print("Welcome to the tip calculator")
total = float(input("What was the total bill? "))
percentage = float(input("What percentage would you like to give? 10, 12, or 15 "))
amount_of_people = int(input("How many people to split the bill? "))



total_each_person = (((percentage / 100) * total) + total) / amount_of_people


print("Each person should pay: $",round(total_each_person, 2))