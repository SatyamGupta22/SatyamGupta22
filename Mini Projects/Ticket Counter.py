print ("Welcome to rollercoaster. Get your ticket here");

height = int(input("Enter your height in cm "));

bill = 0
if height >= 120:
    age = int(input("Enter your age "));
    if age < 12:
        bill = 5
        print ("Please pay $5 for children's ticket")
    
    elif age <= 18:
        bill =  7 
        print ("Please pay $7 for teenager's ticket")
    
    elif age >= 45 and age <= 60:
        print ("Your bill is on the house. Enjoy the ride for free")
    
    else:
        bill = 12
        print ("Please pay $12 for adult ticket")
        
    ticket = input ("Would you like to get your pciture clicked? ");

    if ticket == "yes":
        bill += 3
    print (f"Your final bill is {bill}");
    
else:
    print("You are not ready for the ride");