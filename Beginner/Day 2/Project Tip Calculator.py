print("Welcone to the tip calculator!!")
total_bill = float(input("What was the total bill? $"))
tip_perc = int(input("How much tip would you like to give? 10, 12, or 15? "))
amnt_people = int(input("How many people to split the bill? "))
tip_perc /= 100
tip_perc += 1
pay = (total_bill * tip_perc) / amnt_people
print(f"Each person should pay: ${round(pay,2)}")