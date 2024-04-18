def calculate_discounted_price(price, discount):
    discount_amount = (discount / 100) * price
    discounted_price = price - discount_amount
    return discounted_price

price = 150
discount = 15%


price = float(input("Enter the price: "))
discount = float(input("Enter the discount percentage: "))

discounted_price = calculate_discounted_price(price, discount)

print("Price after discount: ", discounted_price)

