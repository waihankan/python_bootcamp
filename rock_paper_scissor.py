"""
Rock paper scissor game

Scissor beats Paper
Paper beats Rock
Rock beats Scissor

"""
import random

def game():
      """
      Rock paper scissor game
      """
      print("""Rock paper scissor game
            1. Scissor
            2. Rock
            3. Paper
            0. Exit
            """)
      print("Choose one option: ", end = "")

      choice = int(input())
      if choice == 1:
         print("You choose      :Scissor")
         return "Scissor"
      elif choice == 2:
         print("You choose      :Rock")
         return "Rock"
      elif choice == 3:
         print("You choose      :Paper")
         return "Paper"
      elif choice == 0:
         print("Exit")
         return "Exit"
      else:
         print("Invalid choice")
         return "Invalid choice"

def computer():
      """
      Computer choice
      """
      choice = random.randint(1, 3)
      if choice == 1:
         print("Computer choose :Scissor")
         return "Scissor"
      elif choice == 2:
         print("Computer choose :Rock")
         return "Rock"
      elif choice == 3:
         print("Computer choose :Paper")
         return "Paper"
      else:
         print("Invalid choice")
         return "Invalid choice"

def compare(user, computer):
      """
      Compare user and computer choice
      """
      if user == "Scissor" and computer == "Rock":
         print("----Winner: Computer----")
         print("-----------------------\n")
      elif user == "Scissor" and computer == "Paper":
         print("----Winner: You----")
         print("-----------------------\n")
      elif user == "Rock" and computer == "Scissor":
         print("----Winner: You----")
         print("-----------------------\n")
      elif user == "Rock" and computer == "Paper":
         print("----Winner: Computer----")
         print("-----------------------\n")
      elif user == "Paper" and computer == "Scissor":
         print("----Winner: Computer----")
         print("-----------------------\n")
      elif user == "Paper" and computer == "Rock":
         print("----Winner: You----")
         print("-----------------------\n")
      elif user == computer:
         print("----Draw----")
         print("-----------------------\n")
      else:
         print("Invalid choice")
         print("-----------------------\n")

def main():
      """
      Main function
      """
      while True:
         user = game()
         if user == "Exit":
            break
         elif user == "Invalid choice":
            continue
         com = computer()
         compare(user, com)  # User vs computer choice and give the result


if __name__ == "__main__":
      main()
