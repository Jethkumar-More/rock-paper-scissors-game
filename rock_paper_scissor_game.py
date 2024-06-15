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
game = [rock,paper,scissors]
game1 = ["Rock","Paper","Scissor"]
a = int(input(
        "Welcome to our Rock Paper Scissor Game :)\n Please choose between 0 for Rock, 1 for Paper, 2 for Scissor\n"))
if a > 2 or a < 0:
    print("You choose an invalid number!!! 😒\n", "You lose")
else:
    print(f"Player 1 choose: \n{game1[a]}{game[a]}")
    b = random.randint(0,2)
    print(f"Computer Chose:\n{game1[b]}\n{game[b]}")
    if a == b:
        print("It's a draw!!\n Better luck next time!!")
    elif a == 0 and b == 2:
            print("You Won!! 🎉🎉")
    elif a == 2 and b==0:
            print("You lose!!😔\n Better luck next time!!"
                  "")
    elif a < b:
        print("You lose!!😔")
    elif a > b:
        print("You Won!! 🎉🎉")