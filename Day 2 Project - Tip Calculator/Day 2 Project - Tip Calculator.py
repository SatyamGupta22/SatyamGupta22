print ("Welcome to Tip Calculator");

bill = float(input("What is the billed amount? "))
tip = int(input("What perecntage would you give? 10, 12, 15 "));
people = int(input("How many people will split the bill? "));

tip_as_percentage = (tip / 100)
total_tip_amount = (bill * tip_as_percentage)
total_bill = (bill + total_tip_amount)
bill_per_person = (total_bill / people)
final_amount = (bill_per_person)

print(f"Each person should pay {final_amount} ");