import logging

from telegram import (
    Update
)

from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler
)

# ==========================================
# CONFIG
# ==========================================

from config import BOT_TOKEN

# ==========================================
# INLINE MENU
# ==========================================

from inline_buttons import (
    inline_menu
)

# ==========================================
# CLAN COMMANDS
# ==========================================

from clan import (
    claninfo,
    members,
    donation,
    topdonator
)

# ==========================================
# WAR COMMANDS
# ==========================================

from war import (
    war,
    warinfo,
    remain,
    missed
)

# ==========================================
# CWL COMMANDS
# ==========================================

from cwl import (
    cwl,
    cwlremain,
    cwlstars
)

# ==========================================
# PLAYER COMMAND
# ==========================================

from player import (
    player
)

# ==========================================
# WAR LOGS
# ==========================================

from war_logs import (
    warlogs
)

# ==========================================
# AUTO SYSTEMS
# ==========================================

from scheduler import (
    auto_war_check
)

from auto_reminder import (
    auto_attack_reminder
)

from member_tracker import (
    member_tracker
)

# ==========================================
# LOGGING
# ==========================================

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# ==========================================
# START COMMAND
# ==========================================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = (
        "🤖 COC CLAN BOT ONLINE\n\n"

        "Use buttons below "
        "to control bot."
    )

    await update.message.reply_text(
        text,
        reply_markup=inline_menu()
    )

# ==========================================
# HELP COMMAND
# ==========================================

async def help_cmd(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = (
        "🤖 AVAILABLE COMMANDS\n\n"

        "🏰 CLAN COMMANDS\n"
        "/claninfo\n"
        "/members\n"
        "/donation\n"
        "/topdonator\n\n"

        "⚔️ WAR COMMANDS\n"
        "/war\n"
        "/warinfo\n"
        "/remain\n"
        "/missed\n"
        "/warlogs\n\n"

        "🏆 CWL COMMANDS\n"
        "/cwl\n"
        "/cwlremain\n"
        "/cwlstars\n\n"

        "👤 PLAYER COMMAND\n"
        "/player #TAG\n\n"

        "ℹ️ BASIC COMMANDS\n"
        "/start\n"
        "/help"
    )

    await update.message.reply_text(
        text,
        reply_markup=inline_menu()
    )

# ==========================================
# BUTTON CALLBACKS
# ==========================================

async def button_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()

    data = query.data

    # ======================================
    # CLAN INFO
    # ======================================

    if data == "claninfo":

        await claninfo(update, context)

    # ======================================
    # WAR
    # ======================================

    elif data == "war":

        await war(update, context)

    # ======================================
    # CWL
    # ======================================

    elif data == "cwl":

        await cwl(update, context)

    # ======================================
    # WAR LOGS
    # ======================================

    elif data == "warlogs":

        await warlogs(update, context)

    # ======================================
    # HELP
    # ======================================

    elif data == "help":

        await help_cmd(update, context)

    # ======================================
    # PLAYER
    # ======================================

    elif data == "player":

        await query.message.reply_text(
            "Usage:\n/player #TAG"
        )

# ==========================================
# MAIN FUNCTION
# ==========================================

def main():

    # ======================================
    # CREATE BOT
    # ======================================

    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )

    # ======================================
    # BASIC COMMANDS
    # ======================================

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("help", help_cmd)
    )

    # ======================================
    # CLAN COMMANDS
    # ======================================

    app.add_handler(
        CommandHandler("claninfo", claninfo)
    )

    app.add_handler(
        CommandHandler("members", members)
    )

    app.add_handler(
        CommandHandler("donation", donation)
    )

    app.add_handler(
        CommandHandler("topdonator", topdonator)
    )

    # ======================================
    # WAR COMMANDS
    # ======================================

    app.add_handler(
        CommandHandler("war", war)
    )

    app.add_handler(
        CommandHandler("warinfo", warinfo)
    )

    app.add_handler(
        CommandHandler("remain", remain)
    )

    app.add_handler(
        CommandHandler("missed", missed)
    )

    app.add_handler(
        CommandHandler("warlogs", warlogs)
    )

    # ======================================
    # CWL COMMANDS
    # ======================================

    app.add_handler(
        CommandHandler("cwl", cwl)
    )

    app.add_handler(
        CommandHandler("cwlremain", cwlremain)
    )

    app.add_handler(
        CommandHandler("cwlstars", cwlstars)
    )

    # ======================================
    # PLAYER COMMAND
    # ======================================

    app.add_handler(
        CommandHandler("player", player)
    )

    # ======================================
    # INLINE BUTTON HANDLER
    # ======================================

    app.add_handler(
        CallbackQueryHandler(
            button_callback
        )
    )

    # ======================================
    # AUTO WAR CHECKER
    # ======================================

    app.job_queue.run_repeating(
        auto_war_check,
        interval=60,
        first=10
    )

    # ======================================
    # AUTO ATTACK REMINDER
    # ======================================

    app.job_queue.run_repeating(
        auto_attack_reminder,
        interval=1800,
        first=30
    )

    # ======================================
    # MEMBER TRACKER
    # ======================================

    app.job_queue.run_repeating(
        member_tracker,
        interval=5,
        first=3
    )

    # ======================================
    # START BOT
    # ======================================

    print("BOT RUNNING...")

    app.run_polling()

# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":
    main()