from utils import get_clan_data
from config import GROUP_ID

# ==========================================
# SAVE OLD DATA
# ==========================================

old_members = {}

# ==========================================
# MEMBER TRACKER
# ==========================================

async def member_tracker(context):

    global old_members

    print("MEMBER TRACKER RUNNING")

    data = get_clan_data()

    if not data:

        print("NO CLAN DATA")

        return

    member_list = data.get(
        "memberList",
        []
    )

    current_members = {}

    # ======================================
    # SAVE CURRENT MEMBERS
    # ======================================

    for member in member_list:

        tag = member.get("tag")

        current_members[tag] = {

            "name": member.get("name"),

            "role": member.get("role")
        }

    print("CURRENT MEMBERS =", len(current_members))

    # ======================================
    # FIRST RUN
    # ======================================

    if not old_members:

        old_members = current_members

        print("FIRST MEMBER SAVE")

        return

    # ======================================
    # NEW MEMBER
    # ======================================

    for tag, info in current_members.items():

        if tag not in old_members:

            print("NEW MEMBER DETECTED")

            await context.bot.send_message(
                chat_id=GROUP_ID,
                text=(
                    "✅ NEW MEMBER JOINED\n\n"
                    f"👤 {info['name']}"
                )
            )

    # ======================================
    # LEFT MEMBER
    # ======================================

    for tag, info in old_members.items():

        if tag not in current_members:

            print("LEFT MEMBER DETECTED")

            await context.bot.send_message(
                chat_id=GROUP_ID,
                text=(
                    "❌ MEMBER LEFT CLAN\n\n"
                    f"👤 {info['name']}"
                )
            )

    # ======================================
    # ROLE CHANGE
    # ======================================

    for tag, info in current_members.items():

        if tag in old_members:

            old_role = old_members[tag]["role"]

            new_role = info["role"]

            if old_role != new_role:

                print("ROLE CHANGE DETECTED")

                await context.bot.send_message(
                    chat_id=GROUP_ID,
                    text=(
                        "🏅 ROLE UPDATED\n\n"

                        f"👤 {info['name']}\n\n"

                        f"⬅️ {old_role}\n"
                        f"➡️ {new_role}"
                    )
                )

    # ======================================
    # UPDATE OLD DATA
    # ======================================

    old_members = current_members

    print("MEMBER DATA UPDATED")