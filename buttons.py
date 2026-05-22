from telegram import (
    ReplyKeyboardMarkup
)

# ==========================================
# MAIN MENU BUTTONS
# ==========================================

def main_menu():

    keyboard = [

        [
            "🏰 Clan Info",
            "⚔️ War"
        ],

        [
            "🏆 CWL",
            "👤 Player"
        ],

        [
            "📜 War Logs",
            "❓ Help"
        ]
    ]

    return ReplyKeyboardMarkup(

        keyboard,

        resize_keyboard=True
    )