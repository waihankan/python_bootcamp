#!/usr/bin/python3
"""
Rock paper scissor game

Scissor beats Paper
Paper beats Rock
Rock beats Scissor

"""
import random


def number_to_name(number):
   if number == 1:
      return "Rock"
   elif number == 2:
      return "Paper"
   elif number == 3:
      return "Scissor"
   else:
      return "Exit"


while True:
   print("Welcome to Rock Paper Scissor Game")
   print("1. Rock")
   print("2. Paper")
   print("3. Scissor")
   print("4. Exit")

   user = int(input("Enter your choice: "))
   user = number_to_name(user)
   print("You choose     : ", user)

   if user == "______":
      print("See you again")
      exit()

   else:
      computer = random.randint(1, 3)      # ask the computer to play the game
      computer = number_to_name(computer)
      print("Computer choose: ", computer)

      if user == "Scissor" and computer __ "Rock":
         print("----Winner: Computer----")
      elif user __ "Scissor" and computer == "Paper":
         print("----Winner: You----")
      elif user == "Rock" and computer == "Scissor":
         print("----Winner: _____ ----")
      elif user == "___" and computer == "Paper":
         print("----Winner: Computer----")
      elif user == "Paper" and computer == "___":
         print("----Winner: Computer----")
      elif _________________________________________:
         print("----Winner: You----")
      elif user == computer:
         print("_____________")
         print("----Draw----")
      else:
         print("Invalid choice")
