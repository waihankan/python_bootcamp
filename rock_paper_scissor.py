#!/usr/bin/python3
"""
Rock paper scissor game

Scissor beats Paper
Paper beats Rock
Rock beats Scissor

"""
import random


print("Welcome to Rock Paper Scissor Game")
print("1. Rock")
print("2. Paper")
print("3. Scissor")
print("4. Exit")

def number_to_name(number):
   if number == 1:
      return "Rock"
   elif number == 2:
      return "Paper"
   elif number == 3:
      return "Scissor"
   else:
      return "Exit"

user = int(input("Enter your choice: "))
user = number_to_name(user)
print("You choose     : ", user)

if user == "Exit":
   print("See you again")
   exit()

else:
   computer = random.randint(1, 3)
   computer = number_to_name(computer)
   print("Computer choose: ", computer)

   if user == "Scissor" and computer == "Rock":
      print("----Winner: Computer----")
   elif user == "Scissor" and computer == "Paper":
      print("----Winner: You----")
   elif user == "Rock" and computer == "Scissor":
      print("----Winner: You----")
   elif user == "Rock" and computer == "Paper":
      print("----Winner: Computer----")
   elif user == "Paper" and computer == "Scissor":
      print("----Winner: Computer----")
   elif user == "Paper" and computer == "Rock":
      print("----Winner: You----")
   elif user == computer:
      print("----Draw----")
   else:
      print("Invalid choice")
