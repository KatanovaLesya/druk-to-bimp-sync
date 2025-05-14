import requests
import os
from dotenv import load_dotenv

load_dotenv()

BIMP_URL = os.getenv("BIMP_URL")
BIMP_EMAIL = os.getenv("BIMP_EMAIL")
BIMP_PASSWORD = os.getenv("BIMP_PASSWORD")

def login_bimp():
    url = f"{BIMP_URL}/org2/auth/api-login"
    payload = {
        "email": BIMP_EMAIL,
        "password": BIMP_PASSWORD
    }
    headers = {
        "accept-language": "uk-UA"
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()["data"]["accessToken"]
