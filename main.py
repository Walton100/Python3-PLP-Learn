def calculate_discount(price, discount_percent):
    new_price = 0

    if discount_percent >= 20:
        new_price = price * (1 - (discount_percent / 100))
    print(f'The final price is {new_price}')


price=float(input('Enter original price:'))
discount_percent=float(input('Enter discount percent:'))

calculate_discount(price,discount_percent)

