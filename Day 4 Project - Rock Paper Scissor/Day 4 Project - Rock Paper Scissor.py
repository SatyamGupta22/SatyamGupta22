import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# User Logic

game_image = [rock, paper, scissors]
user_choice = int(input("What will you choose? Type 0 for rock, 1 for paper or 2 for scissors. "))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you  lose")
print(game_image[user_choice])

# Computer Logic

computer_choice = random.randint(0, 2)
print("Computer chose: ")
print(game_image[computer_choice])

# Logic

if user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif user_choice == 2 and computer_choice == 0:
    print("You Lose!")
elif user_choice > computer_choice:
    print("You Win!")
elif computer_choice > user_choice:
    print("You Lose!")
elif computer_choice == user_choice:
    print("It's a Draw!")
