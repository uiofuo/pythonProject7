ticket = int(input("Ввести колияество билетов : "))
price = 0
for value in range(ticket):
    age = int(input("Ввести возраст"))
    if 18 <= age <= 25:
        price = price + 990
        print("Сумма покупки", price, "p")
    elif 18 < age:
        price = price + 0
        print("Сумма покупки", price, "p")
    elif age > 25:
        price = price + 1390
        print("Сумма покупки", price, "p")
if ticket > 3:
    price = price - (price / 10)
print("Итоговая цена билетов со скидкой ", int(price), "p")
