from telegram import Update
from telegram.ext import ContextTypes

from utils import get_war_data

# ==========================================
# CWL STATUS
# ==========================================

async def cwl(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    data = get_war_data()

    if not data:

        await update.message.reply_text(
            "❌ No CWL data found!"
        )

        return

    clan = data.get("clan", {})
    opponent = data.get("opponent", {})

    state = data.get("state")

    text = (
        "🏆 CWL WAR STATUS\n\n"

        f"🏰 Clan: "
        f"{clan.get('name')}\n"

        f"🛡 Opponent: "
        f"{opponent.get('name')}\n\n"

        f"⭐ Clan Stars: "
        f"{clan.get('stars', 0)}\n"

        f"⭐ Enemy Stars: "
        f"{opponent.get('stars', 0)}\n\n"

        f"📊 State: {state}"
    )

    await update.message.reply_text(text)

# ==========================================
# CWL REMAIN
# ==========================================

async def cwlremain(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    data = get_war_data()

    if not data:

        await update.message.reply_text(
            "❌ No CWL data found!"
        )

        return

    state = data.get("state")

    if state != "inWar":

        await update.message.reply_text(
            "⚠️ CWL battle day is not active."
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
                f"❌ {member['name']} → attack not used"
            )

        else:

            remain_list.append(
                f"✅ {member['name']} → completed"
            )

    text = (
        "🏆 CWL ATTACK STATUS\n\n"
        + "\n".join(remain_list)
    )

    await update.message.reply_text(text)

# ==========================================
# CWL STARS
# ==========================================

async def cwlstars(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    data = get_war_data()

    if not data:

        await update.message.reply_text(
            "❌ No CWL data found!"
        )

        return

    clan = data.get("clan", {})

    members = clan.get("members", [])

    stars_list = []

    for member in members:

        total_stars = 0

        for attack in member.get(
            "attacks",
            []
        ):

            total_stars += attack.get(
                "stars",
                0
            )

        stars_list.append(
            (
                member["name"],
                total_stars
            )
        )

    stars_list.sort(
        key=lambda x: x[1],
        reverse=True
    )

    text = "🏆 CWL STAR LEADERBOARD\n\n"

    for i, player in enumerate(
        stars_list,
        1
    ):

        text += (
            f"{i}. {player[0]} "
            f"→ {player[1]}⭐\n"
        )

    await update.message.reply_text(text)