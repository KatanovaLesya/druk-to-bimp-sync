import requests

def fetch_druk_orders(token, typography_id):
    url = f"https://api.newmedia.ua/api/typographies/{typography_id}/orders"

    params = {
        "sort": "new",
        "direction": "desc",
        "without_inc": 1
    }
    headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json"
}


    response = requests.get(url, params=params, headers=headers)

    print("=== RAW RESPONSE ===")
    print("Status code:", response.status_code)
    print("Text:", response.text)
    print("====================")

    response.raise_for_status()
    return response.json()["list"]




