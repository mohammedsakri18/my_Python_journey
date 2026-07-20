price = int(input("Enter product price: "))
percentage = float(input("Enter discount percentage: "))

discount_amount = (price * percentage) / 100
final_price = price - discount_amount

print(f"Discount Amount: {discount_amount:.2f}")
print(f"Final Price: {final_price:.2f}")