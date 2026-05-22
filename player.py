from telegram import Update
from telegram.ext import ContextTypes

from utils import get_player_data

# ==========================================
# PLAYER INFO
# ==========================================

async def player(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    # ======================================
    # CHECK TAG
    # ======================================

    if len(context.args) == 0:

        await update.message.reply_text(
            "Usage:\n/player #TAG"
        )

        return

    # ======================================
    # GET TAG
    # ======================================

    player_tag = context.args[0]

    # ======================================
    # FETCH DATA
    # ======================================

    data = get_player_data(player_tag)

    if not data:

        await update.message.reply_text(
            "❌ Player not found!"
        )

        return

    # ======================================
    # HEROES
    # ======================================

    heroes_text = ""

    heroes = data.get("heroes", [])

    for hero in heroes:

        heroes_text += (
            f"{hero.get('name')} "
            f"(Lv {hero.get('level')})\n"
        )

    # ======================================
    # FINAL TEXT
    # ======================================

    text = (
        f"👤 PLAYER INFO\n\n"

        f"🏷 Name: "
        f"{data.get('name')}\n"

        f"🏰 Town Hall: "
        f"{data.get('townHallLevel')}\n"

        f"🏆 Trophies: "
        f"{data.get('trophies')}\n"

        f"⭐ War Stars: "
        f"{data.get('warStars')}\n"

        f"🤝 Donations: "
        f"{data.get('donations')}\n\n"

        f"🦸 HEROES\n"
        f"{heroes_text}"
    )

    await update.message.reply_text(text)