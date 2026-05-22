from telegram import Update
from telegram.ext import ContextTypes

from utils import (
    get_clan_data
)

# ==========================================
# CLAN INFO
# ==========================================

async def claninfo(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    data = get_clan_data()

    if not data:

        await update.message.reply_text(
            "❌ Failed to load clan info!"
        )

        return

    text = (
        f"🏰 Clan: {data.get('name')}\n"
        f"⭐ Level: {data.get('clanLevel')}\n"
        f"👥 Members: {data.get('members')}/50\n"
        f"🏆 Points: {data.get('clanPoints')}\n"
        f"⚔️ War Wins: {data.get('warWins')}\n"
        f"🌍 Location: "
        f"{data.get('location', {}).get('name')}"
    )

    await update.message.reply_text(text)

# ==========================================
# MEMBERS
# ==========================================

async def members(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    data = get_clan_data()

    if not data:

        await update.message.reply_text(
            "❌ Failed to load members!"
        )

        return

    member_list = data.get("memberList", [])

    if not member_list:

        await update.message.reply_text(
            "No members found!"
        )

        return

    text = "👥 MEMBER LIST\n\n"

    for member in member_list[:30]:

        text += (
            f"{member['name']} | "
            f"{member.get('role')} | "
            f"{member.get('trophies')}🏆\n"
        )

    await update.message.reply_text(text)

# ==========================================
# DONATION
# ==========================================

async def donation(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    data = get_clan_data()

    if not data:

        await update.message.reply_text(
            "❌ Failed to load donation data!"
        )

        return

    members_data = data.get("memberList", [])

    sorted_members = sorted(
        members_data,
        key=lambda x: x.get("donations", 0),
        reverse=True
    )

    text = "🤝 TOP DONATORS\n\n"

    for i, member in enumerate(
        sorted_members[:10],
        1
    ):

        text += (
            f"{i}. {member['name']} → "
            f"{member.get('donations', 0)}\n"
        )

    await update.message.reply_text(text)

# ==========================================
# TOP DONATOR
# ==========================================

async def topdonator(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await donation(update, context)