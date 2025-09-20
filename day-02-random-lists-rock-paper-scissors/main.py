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
import random
choose = int(input("Choose: rock, paper, scissors: "))
pilihan = [rock, paper, scissors]
npc = random.choice([rock, paper, scissors])

print(pilihan[choose])
print(npc)

if pilihan[choose] == rock:
    if npc == scissors:
        print("You win!")
    elif npc == paper:
        print("You lose!")
    else:
        print("You draw!")

elif pilihan[choose] == paper:
    if npc == scissors:
        print("You lose!")
    elif npc == paper:
        print("You draw!")
    else:
        print("You win!")

elif pilihan[choose] == scissors:
    if npc == scissors:
        print("You draw!")
    elif npc == paper:
        print("You win!")
    else:
        print("You lose!")