import requests

from config import (
    COC_API_TOKEN,
    CLAN_TAG
)

# ==========================================
# API CONFIG
# ==========================================

CLAN_TAG_ENCODED = "%23" + CLAN_TAG.replace("#", "")

BASE_URL = (
    f"https://api.clashofclans.com/v1/clans/{CLAN_TAG_ENCODED}"
)

HEADERS = {
    "Authorization": f"Bearer {COC_API_TOKEN}"
}

# ==========================================
# GET CLAN DATA
# ==========================================

def get_clan_data():

    try:

        response = requests.get(
            BASE_URL,
            headers=HEADERS,
            timeout=10
        )

        print("CLAN STATUS:", response.status_code)

        if response.status_code == 200:

            data = response.json()

            print(data)

            return data

        print(response.text)

    except Exception as e:

        print("CLAN ERROR:", e)

    return None

# ==========================================
# GET WAR DATA
# ==========================================

def get_war_data():

    try:

        url = f"{BASE_URL}/currentwar"

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=10
        )

        print("WAR STATUS:", response.status_code)

        if response.status_code == 200:

            data = response.json()

            print("WAR DATA:", data)

            # ==============================
            # VALID WAR STATES
            # ==============================

            state = data.get("state")

            print("WAR STATE:", state)

            if state in [
                "notInWar",
                "preparation",
                "inWar",
                "warEnded"
            ]:

                return data

        print("WAR RESPONSE:", response.text)

    except Exception as e:

        print("WAR ERROR:", e)

    return None

# ==========================================
# GET PLAYER DATA
# ==========================================

def get_player_data(player_tag):

    try:

        player_tag_encoded = (
            player_tag.replace("#", "%23")
        )

        url = (
            "https://api.clashofclans.com/v1/"
            f"players/{player_tag_encoded}"
        )

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=10
        )

        print(
            "PLAYER STATUS:",
            response.status_code
        )

        if response.status_code == 200:

            data = response.json()

            print(data)

            return data

        print(response.text)

    except Exception as e:

        print("PLAYER ERROR:", e)

    return None