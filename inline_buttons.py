from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

# ==========================================
# INLINE MENU
# ==========================================

def inline_menu():

    keyboard = [

        [
            InlineKeyboardButton(
                "🏰 Clan Info",
                callback_data="claninfo"
            ),

            InlineKeyboardButton(
                "⚔️ War",
                callback_data="war"
            )
        ],

        [
            InlineKeyboardButton(
                "🏆 CWL",
                callback_data="cwl"
            ),

            InlineKeyboardButton(
                "👤 Player",
                callback_data="player"
            )
        ],

        [
            InlineKeyboardButton(
                "📜 War Logs",
                callback_data="warlogs"
            ),

            InlineKeyboardButton(
                "❓ Help",
                callback_data="help"
            )
        ]
    ]

    return InlineKeyboardMarkup(
        keyboard
    )