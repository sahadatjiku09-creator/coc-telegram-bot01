import sqlite3

from telegram import Update
from telegram.ext import ContextTypes

from utils import get_war_data

# ==========================================
# DATABASE
# ==========================================

conn = sqlite3.connect(
    "war_logs.db",
    check_same_thread=False
)

cursor = conn.cursor()

# ==========================================
# TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS war_logs (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    opponent TEXT,

    clan_stars INTEGER,

    enemy_stars INTEGER,

    destruction REAL,

    result TEXT
)
""")

conn.commit()

# ==========================================
# SAVE WAR LOG
# ==========================================

def save_war_log():

    data = get_war_data()

    if not data:
        return

    state = data.get("state")

    # ONLY SAVE WHEN WAR ENDED

    if state != "warEnded":
        return

    clan = data.get("clan", {})

    opponent = data.get("opponent", {})

    clan_stars = clan.get("stars", 0)

    enemy_stars = opponent.get("stars", 0)

    destruction = clan.get(
        "destructionPercentage",
        0
    )

    # ======================================
    # RESULT
    # ======================================

    if clan_stars > enemy_stars:

        result = "WIN"

    elif clan_stars < enemy_stars:

        result = "LOSE"

    else:

        result = "DRAW"

    # ======================================
    # INSERT
    # ======================================

    cursor.execute("""

    INSERT INTO war_logs (

        opponent,
        clan_stars,
        enemy_stars,
        destruction,
        result

    )

    VALUES (?, ?, ?, ?, ?)

    """, (

        opponent.get("name"),

        clan_stars,

        enemy_stars,

        destruction,

        result
    ))

    conn.commit()

    print("WAR LOG SAVED")

# ==========================================
# SHOW WAR LOGS
# ==========================================

async def warlogs(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    cursor.execute("""

    SELECT opponent,
           clan_stars,
           enemy_stars,
           destruction,
           result

    FROM war_logs

    ORDER BY id DESC

    LIMIT 10

    """)

    logs = cursor.fetchall()

    if not logs:

        await update.message.reply_text(
            "❌ No war logs found!"
        )

        return

    text = "📜 LAST 10 WAR LOGS\n\n"

    for log in logs:

        text += (
            f"🛡 Opponent: {log[0]}\n"

            f"⭐ Score: "
            f"{log[1]} - {log[2]}\n"

            f"💥 Destruction: "
            f"{log[3]}%\n"

            f"🏆 Result: {log[4]}\n\n"
        )

    await update.message.reply_text(text)