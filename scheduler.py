from utils import get_war_data

from config import GROUP_ID

from database import (
    save_war_state,
    get_saved_war_state
)

# ==========================================
# AUTO WAR CHECK
# ==========================================

async def auto_war_check(context):

    data = get_war_data()

    if not data:
        return

    current_state = data.get("state")

    if not current_state:
        return

    # ======================================
    # GET OLD STATE
    # ======================================

    old_state = get_saved_war_state()

    print("OLD STATE =", old_state)

    print("CURRENT STATE =", current_state)

    # ======================================
    # FIRST SAVE
    # ======================================

    if old_state is None:

        save_war_state(current_state)

        print("FIRST STATE SAVED")

        return

    # ======================================
    # SAME STATE
    # ======================================

    if old_state == current_state:

        print("NO STATE CHANGE")

        return

    # ======================================
    # SAVE NEW STATE
    # ======================================

    save_war_state(current_state)

    # ======================================
    # PREPARATION
    # ======================================

    if current_state == "preparation":

        clan = data.get("clan", {})

        opponent = data.get(
            "opponent",
            {}
        )

        text = (
            "⚔️ WAR PREPARATION STARTED!\n\n"

            f"🏰 Clan: "
            f"{clan.get('name')}\n"

            f"🛡 Opponent: "
            f"{opponent.get('name')}"
        )

        await context.bot.send_message(
            chat_id=GROUP_ID,
            text=text
        )

        print("PREPARATION MESSAGE SENT")

    # ======================================
    # WAR STARTED
    # ======================================

    elif current_state == "inWar":

        await context.bot.send_message(
            chat_id=GROUP_ID,
            text="⚔️ WAR STARTED!"
        )

        print("WAR START MESSAGE SENT")

    # ======================================
    # WAR ENDED
    # ======================================

    elif current_state == "warEnded":

        await context.bot.send_message(
            chat_id=GROUP_ID,
            text="🏁 WAR ENDED!"
        )

        print("WAR END MESSAGE SENT")

    # ======================================
    # NOT IN WAR
    # ======================================

    elif current_state == "notInWar":

        await context.bot.send_message(
            chat_id=GROUP_ID,
            text="⚠️ Clan is not currently in war."
        )

        print("NOT IN WAR MESSAGE SENT")