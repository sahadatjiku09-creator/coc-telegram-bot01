from telegram import Update
from telegram.ext import ContextTypes

from utils import get_war_data

# ==========================================
# WAR
# ==========================================

async def war(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    data = get_war_data()

    print("WAR DATA =", data)

    # ======================================
    # NO DATA
    # ======================================

    if not data:

        await update.message.reply_text(
            "❌ No war data found!"
        )

        return

    # ======================================
    # GET STATE
    # ======================================

    state = data.get("state")

    print("WAR STATE =", state)

    # ======================================
    # SEARCHING / NO WAR
    # ======================================

    if state == "notInWar":

        await update.message.reply_text(
            "⚠️ Clan is not currently in war."
        )

        return

    # ======================================
    # PREPARATION
    # ======================================

    if state == "preparation":

        clan = data.get("clan", {})
        opponent = data.get("opponent", {})

        text = (
            "⚔️ WAR PREPARATION DAY\n\n"

            f"🏰 Clan: "
            f"{clan.get('name')}\n"

            f"🛡 Opponent: "
            f"{opponent.get('name')}\n\n"

            "⏳ Battle day has not started yet."
        )

        await update.message.reply_text(text)

        return

    # ======================================
    # ACTIVE WAR
    # ======================================

    if state == "inWar":

        clan = data.get("clan", {})
        opponent = data.get("opponent", {})

        text = (
            "⚔️ CURRENT WAR\n\n"

            f"🏰 {clan.get('name')} "
            f"({clan.get('stars', 0)}⭐)\n\n"

            f"🛡 {opponent.get('name')} "
            f"({opponent.get('stars', 0)}⭐)\n\n"

            f"💥 Clan Destruction: "
            f"{clan.get('destructionPercentage', 0)}%\n"

            f"💥 Enemy Destruction: "
            f"{opponent.get('destructionPercentage', 0)}%"
        )

        await update.message.reply_text(text)

        return

    # ======================================
    # WAR ENDED
    # ======================================

    if state == "warEnded":

        await update.message.reply_text(
            "🏁 WAR ENDED!"
        )

        return

    # ======================================
    # UNKNOWN
    # ======================================

    await update.message.reply_text(
        f"UNKNOWN WAR STATE: {state}"
    )

# ==========================================
# WAR INFO
# ==========================================

async def warinfo(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    data = get_war_data()

    if not data:

        await update.message.reply_text(
            "❌ No war info found!"
        )

        return

    clan = data.get("clan", {})
    opponent = data.get("opponent", {})

    text = (
        "⚔️ WAR DETAILS\n\n"

        f"🏰 Clan: {clan.get('name')}\n"
        f"🛡 Opponent: {opponent.get('name')}\n\n"

        f"⭐ Clan Stars: "
        f"{clan.get('stars', 0)}\n"

        f"⭐ Enemy Stars: "
        f"{opponent.get('stars', 0)}"
    )

    await update.message.reply_text(text)

# ==========================================
# REMAIN
# ==========================================

async def remain(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    data = get_war_data()

    if not data:

        await update.message.reply_text(
            "❌ No war data found!"
        )

        return

    state = data.get("state")

    if state != "inWar":

        await update.message.reply_text(
            "⚠️ Battle day is not active yet."
        )

        return

    clan = data.get("clan", {})

    remain_list = []

    for member in clan.get("members", []):

        attacks = len(
            member.get("attacks", [])
        )

        if attacks == 0:

            remain_list.append(
                f"❌ {member['name']} → 2 attacks left"
            )

        elif attacks == 1:

            remain_list.append(
                f"⚠️ {member['name']} → 1 attack left"
            )

        else:

            remain_list.append(
                f"✅ {member['name']} → completed"
            )

    text = (
        "⚔️ WAR ATTACK STATUS\n\n"
        + "\n".join(remain_list)
    )

    await update.message.reply_text(text)

# ==========================================
# MISSED
# ==========================================

async def missed(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    data = get_war_data()

    if not data:

        await update.message.reply_text(
            "❌ No war data found!"
        )

        return

    state = data.get("state")

    if state != "inWar":

        await update.message.reply_text(
            "⚠️ Battle day is not active yet."
        )

        return

    clan = data.get("clan", {})

    missed_players = []

    for member in clan.get("members", []):

        attacks = len(
            member.get("attacks", [])
        )

        if attacks == 0:

            missed_players.append(
                f"❌ {member['name']}"
            )

    if not missed_players:

        await update.message.reply_text(
            "✅ Nobody missed attacks!"
        )

        return

    text = (
        "❌ MISSED ATTACKS\n\n"
        + "\n".join(missed_players)
    )

    await update.message.reply_text(text)