import sqlite3

# ==========================================
# CONNECT DATABASE
# ==========================================

conn = sqlite3.connect(
    "bot.db",
    check_same_thread=False
)

cursor = conn.cursor()

# ==========================================
# CREATE TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS war_state (
    id INTEGER PRIMARY KEY,
    state TEXT
)
""")

conn.commit()

# ==========================================
# SAVE WAR STATE
# ==========================================

def save_war_state(state):

    cursor.execute(
        "DELETE FROM war_state"
    )

    cursor.execute(
        "INSERT INTO war_state(state) VALUES(?)",
        (state,)
    )

    conn.commit()

# ==========================================
# GET WAR STATE
# ==========================================

def get_saved_war_state():

    cursor.execute(
        "SELECT state FROM war_state LIMIT 1"
    )

    result = cursor.fetchone()

    if result:

        return result[0]

    return None