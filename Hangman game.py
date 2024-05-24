import random

word_list= ["apple", "banana", "cherry"]
lives=6
choseen = random.choice(word_list)
print(choseen)

display=[]
for i in range(len(choseen)):
    display += '_'
print(display)
gameover=False

while not gameover:

    guessed_letter = input("Guess a letter: ").lower()
    for position  in range(len(choseen)):
        letter=choseen[position]
        if letter == guessed_letter:
           display[position]=guessed_letter
    print(display,lives)
    if guessed_letter not in choseen:
        lives -=1
        if lives==0:
            gameover=True
            print("You lost!")

    if '_' not in display:
        gameover=True
        print("You won!")









