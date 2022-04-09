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

#Write your code below this line 👇
import random

weapons = ['rock', 'paper', 'scissors']

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
user_weapon = weapons[user_choice]

computer_choice = random.randint(0,2)
computer_weapon = weapons[computer_choice]


def weapon(user, value):
  if value == 'rock':
    print(user, rock)
  if value == 'paper':
    print(user, paper)
  if value == 'scissors':
    print(user, scissors)

weapon('User', user_weapon)
weapon('Computer', computer_weapon)

def winner(which_user):
  if which_user == 'Tie':
    print("TIE !!!")
  elif which_user == 'User':
    print("USER  WINS !!!")
  elif which_user == 'Computer':
    print("COMPUTER WINS !!!")
  else:
    print("?????")



if user_weapon == 'rock' and computer_weapon == 'rock': winner('Tie')
if user_weapon == 'paper' and computer_weapon == 'paper': winner('Tie')
if user_weapon == 'scissors' and computer_weapon == 'scissors': winner('Tie')
  
if user_weapon == 'rock' and computer_weapon == 'scissors': winner('User')
if user_weapon == 'scissors' and computer_weapon == 'paper': winner('User')
if user_weapon == 'paper' and computer_weapon == 'rock': winner('User')
  
if computer_weapon == 'rock' and user_weapon == 'scissors': winner('Computer')
if computer_weapon == 'scissors' and user_weapon == 'paper': winner('Computer')
if computer_weapon == 'paper' and user_weapon == 'rock': winner('Computer')