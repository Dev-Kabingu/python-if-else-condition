# defining my function
def calculate_discount(price, discount_percent):
    # check if discount percent is above 20 and calculate the discount amount and the final price
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price  
        final_price = price - discount_amount
        return final_price
    else:
        return price  
price = float(input("Enter the original price of product: "))
discount_percent = float(input("Enter the discount percentage allowed: "))

final_price = calculate_discount(price, discount_percent)

if final_price == price:
    print(f"No discount allowed on the product, price is: ${final_price:.2f}")
else:
    print(f"price after allowing a {discount_percent}% the discount is: ${final_price:.2f}")
