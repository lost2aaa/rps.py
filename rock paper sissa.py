import os
import random

score = 0 # 2 
select = input("your choice?: ")
lists = ['rock', 'paper', 'sciscors']

def rock():
  if select == 'rock':
    computer_choice = random.choice(lists)
    print(f"Computer's choice : {computer_choice}")
    
    if computer_choice == 'rock':
      print('tie')
      
    elif computer_choice == "sciscsors":
      score += 1
      print(select + 'you won!' + score)
      
    elif computer_choice == "paper":
      print(computer_choice + " " +"wins!")
rock()

#paper
def paper():
  if input == 'paper':
    computer_choice = random.choice(lists)
    print(f'computers choice: {computer_choice}')
    
    if computer_choice == 'paper':
      print("tie")
      
    elif computer_choice == 'sciscsors':
      score -= 1
      print(computer_choice +  "wins" + score) 
    
    elif computer_choice == 'rock':
      score += 1
      print(select + " " + 'wins' + score)
paper()

#sciscsros
def sis():
  if select == 'sciscsors':
    computer_choice = random.choice(lists)
    print(f'computers choice : {computer_choice}')
  
    if computer_choice == 'sciscsors':
      print('tie')

    elif computer_choice == 'paper':
      score += 1
      print( select  + "" + "wins!")

    elif computer_choice == 'rock': 
      score -= 1
      print(computer_choice + '' "wins!" + score)
sis()

def scores():
  if score == 2 or score > 2:
    print("You won!")
  else:
    print('you lost')
scores()

