principal = int(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = int(input("Enter time in years: "))
si = (principal * rate * time) / 100


print(f"Simple Interest: {si:.2f}")