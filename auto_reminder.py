from utils import get_war_data

from config import GROUP_ID

# ==========================================
# AUTO REMINDER
# ==========================================

async def auto_attack_reminder(context):

    data = get_war_data()

    if not data:
        return

    state = data.get("state")

    # ======================================
    # ONLY DURING BATTLE DAY
    # ======================================

    if state != "inWar":
        return

    clan = data.get("clan", {})

    remain_list = []

    for member in clan.get("members", []):

        attacks = len(
            member.get("attacks", [])
        )

        # ==============================
        # 0 ATTACKS
        # ==============================

        if attacks == 0:

            remain_list.append(
                f"❌ {member['name']} → 2 attacks left"
            )

        # ==============================
        # 1 ATTACK
        # ==============================

        elif attacks == 1:

            remain_list.append(
                f"⚠️ {member['name']} → 1 attack left"
            )

    # ======================================
    # NO REMAINING ATTACKS
    # ======================================

    if not remain_list:
        return

    text = (
        "⚠️ WAR REMINDER ⚠️\n\n"
        + "\n".join(remain_list)
    )

    await context.bot.send_message(
        chat_id=GROUP_ID,
        text=text
    )

    print("AUTO REMINDER SENT")