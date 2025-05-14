import requests

def send_to_bimp(order, token):
    url = "https://app.bimpsoft.com/org2/customerInvoice/api-insert"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "number": order.get("order_id"),
        "createdAt": order.get("created_at"),
        "clientName": order.get("client", {}).get("name"),
        "comment": order.get("product_title"),
        "total": order.get("total_price"),
        "quantity": order.get("quantity")
    }

    response = requests.post(url, json=payload, headers=headers)

    print(f"[BIMP] {payload['number']} → Status: {response.status_code}")
    if response.status_code != 200:
        print("Response text:", response.text)

    response.raise_for_status()
    return response.json()
