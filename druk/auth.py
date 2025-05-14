import os
import requests

def login_druk():
    url = "https://api.newmedia.ua/api/employees/auth/login"
    payload = {
        "email": os.getenv("DRUK_EMAIL"),
        "password": os.getenv("DRUK_PASSWORD")
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    data = response.json()
    token = data["token"]
    typography_id = str(data["employee"]["typography"]["id"])
    return token, typography_id
