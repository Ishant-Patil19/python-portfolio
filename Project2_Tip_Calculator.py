# Level: Beginner

# Tip Calculator 💸

"""
A beginner-friendly Python script that calculates how much each person should pay 
after splitting a bill, including a customizable tip percentage. 
It demonstrates user input handling, basic math operations, 
and formatting output to two decimal places.
"""

print("Welcome to the tip calculator")
bill = float(input("What was the total bill $ "))
tip = int(input("How much tip would you like to give ? 10 12 15: "))
people = int(input("How many people to split the bill ? : "))
tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
amount_per_person = total_bill / people
final_amount = round(amount_per_person, 2)
print(f"Each person should pay {final_amount}")