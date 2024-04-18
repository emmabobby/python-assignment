discounted_price = price - (price * discount / 100)
    return discounted_price

price = float(input("Enter the price: "))
discount_percentage = float(input("Enter the discount percentage: "))

discounted_price = calculate_discounted_price(price, discount_percentage)

print("The price after discount is", discounted_price)