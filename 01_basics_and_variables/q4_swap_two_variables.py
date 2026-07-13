value1 = int(input("Enter first value: ")) 
value2 = int(input("Enter second value: "))

print(f"Before swapping:\nFirst value: {value1}\nSecond value: {value2}\n")
value1, value2 = value2, value1
print(f"After swapping:\nFirst value: {value1}\nSecond value: {value2}")
