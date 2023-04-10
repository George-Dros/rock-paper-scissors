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

choice = input("Choose Rock, Paper or Scissors? ")
l_choice = choice.lower()
computer_choice = random.randint(0,2)
m_choice =""

if l_choice == "rock":
  l_choice = rock

elif l_choice == "paper":
  l_choice = paper

elif l_choice == "scissors":
  l_choice = scissors

if  computer_choice == 0:
  m_choice = rock
elif   computer_choice == 1:
  m_choice = paper
else:
  m_choice = scissors 

if l_choice == rock  and m_choice == rock:
  print("You Chose:")
  print(l_choice)
  print("Computer chose:")
  print(m_choice)
  print("It's a tie!")

elif l_choice == rock and m_choice == paper:
  print("You Chose:")
  print(l_choice)
  print("Computer chose:")
  print(m_choice)
  print("You Lose!!")

elif l_choice == rock and m_choice == scissors:
  print("You Chose:")
  print(l_choice)
  print("Computer chose:")
  print(m_choice)
  print("You WIN!!")

elif l_choice == paper and m_choice == rock:
  print("You Chose:")
  print(l_choice)
  print("Computer chose:")
  print(m_choice)
  print("You WIN!!")

elif l_choice == paper and m_choice == paper:
  print("You Chose:")
  print(l_choice)
  print("Computer chose:")
  print(m_choice)
  print("It's a tie!")

elif l_choice == paper and m_choice == scissors:
  print("You Chose:")
  print(l_choice)
  print("Computer chose:")
  print(m_choice)
  print("You Lose!")

elif l_choice == scissors and m_choice == rock:
  print("You Chose:")
  print(l_choice)
  print("Computer chose:")
  print(m_choice)
  print("You Lose!")

elif l_choice == scissors and m_choice == paper:
  print("You Chose:")
  print(l_choice)
  print("Computer chose:")
  print(m_choice)
  print("You WIN!!")

elif l_choice == scissors and m_choice == scissors:
  print("You Chose:")
  print(l_choice)
  print("Computer chose:")
  print(m_choice)
  print("It's a tie!")

