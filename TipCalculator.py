print("Welcome to the tip calculator :3")
bill = float(input("What was the total bill?\n$ "))
tip = float(input("How much tip would you like to give? 10, 12, or 15?\n$ "))
people = float(input("How many people to split the bill? $\n$ "))
total = (tip/100 * bill + bill)/people 
print(f"Each person should pay: ${round(total, 2)}")