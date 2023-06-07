# libraries
from getpass import getpass as input

# Intro and names input
print("Let's play Rock, paper, scissors!")
p1 = input("Player 1 name: ")
p2 = input("Player 2 name: ")

# Variables
score_p1 = 0
score_p2 = 0
round = 1
s = "✂️"
p = "🧻"
r = "🗿"

# Game functions
def m():
  print()
  print(p1,p1e,"Vs.",p2,p2e)
  print()
def p1w():
  print()
  print(p1,"wins!🏆")
  print()
def p2w():
  print()
  print(p2,"wins!🏆")
  print()
  
# Game
while True:
  if score_p1 == 3 or score_p2 == 3:
    print("Game finished!")
    print()
    print("Score 🏆")
    print(p1,"->",score_p1)
    print(p2,"->",score_p2)
    print()
    newgame = input("Do you want to play again?")
    if newgame == "y" or newgame == "Y" or newgame == "yES" or newgame == "YES" or newgame == "Yes":
      score_p1 = 0
      score_p2 = 0
      round = 1 
      continue
    else:
      exit()
  else:
    print()
    print("Round:",round)
    print() 
    
    # Player 1 turn 
    print()
    print(p1,"it's your turn!")
    print()
    print("Press 'r' for Rock, 'p' for paper and 's' for scissors")
    print()
    p1e = input()
    p1e_len = len(p1e)
    if p1e_len == 1 and (p1e == 'r' or p1e == 'p' or p1e == 's' or p1e == 'R' or p1e == 'S' or p1e == 'P'):
      # Assigning emoticons for Player 1
      if p1e == "s" or p1e == "S":
        p1e = "✂️"   
      elif p1e == "p" or p1e == "P":
        p1e = "🧻"
      elif p1e == "r" or p1e == "R":
        p1e = "🗿"
        print()
        print("It's your turn",p2,"!")
        print()
    else:
      print("Press only one of these keys: 'r', 'p' or 's'")
      continue
    # Player 2 turn
    p2e = input()
    p2e_len = len(p2e)
    if p2e_len == 1 and (p2e == 'r' or p2e == 'p' or p2e == 's' or p2e == 'R' or p2e == 'S' or p2e == 'P'):   
      round += 1
      # Assigning emoticons for Player 2
  
      if p2e == "s" or p2e == "S":
        p2e = "✂️"   
      elif p2e == "p" or p2e == "P":
        p2e = "🧻"
      else:
        p2e == "r" or p2e == "R"
        p2e = "🗿"
      # Match
      if p1e == p2e:
        m()
        print()
        print("Tied!🙄")
        print()
      elif p1e == p and p2e == s:
        m()
        p2w()
        score_p2 +=1
      elif p1e == p and p2e == r:
        m()
        p1w()
        score_p1 +=1
      elif p1e == r and p2e == p:
        m()
        p2w()
        score_p2 +=1
      elif p1e == r and p2e == s:
        m()
        p1w()
        score_p1 +=1
      elif p1e == s and p2e == p:
        m()
        p1w()
        score_p1 +=1
      else:
        p1e == s and p2e == r
        m()
        p2w()
        score_p2 +=1
    else:
      print("Press only one of these keys: 'r', 'p' or 's'")  
      continue