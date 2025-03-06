try:
    price, status = int(input()), input()
    if price >= 1000 and status == "VIP":
        print("Скидка 25%")
    elif price >= 1000 and status == "обычный":
        print("Скидка 20%")
    elif 500 <= price <= 1000:
        print("Скидка 10%")
    elif price < 500:
        print("Скидка 0%")
except (TypeError, ValueError) as err:
    print(f"Ошибка: {err}")
