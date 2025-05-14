from bimp.auth import login_bimp
from druk.orders import fetch_druk_orders
from druk.auth import login_druk
from bimp.sync import send_to_bimp



bimp_token = login_bimp()
print("Access Token:", bimp_token)

druk_token, typography_id = login_druk()

orders = fetch_druk_orders(druk_token, typography_id)

print("Замовлень отримано:", len(orders))
print("Перше замовлення:", orders[0])

for order in orders:
    send_to_bimp(order, bimp_token)

