import random

rock_paper_scissors = ['rock', 'paper', 'scissors']
rock = rock_paper_scissors[0]
paper = rock_paper_scissors[1]
scissors = rock_paper_scissors[2]

rounds = int(input("How many rounds do you want to play? "))

user_score = 0
computer_score = 0

for i in range(rounds):
    print(f"\nRound {i+1}:")
    selection = input('rock, paper or scissors? ')
    computer_selection = random.choice(rock_paper_scissors)
    print('computer selection: ', computer_selection)
    if selection == paper:
        if computer_selection == paper:
            print('Draw!')
        elif computer_selection == rock:
            print('You win this round!')
            user_score += 1
        elif computer_selection == scissors:
            print('Computer wins this round!')
            computer_score += 1
    elif selection == scissors:
        if computer_selection == scissors:
            print('Draw!')
        elif computer_selection == paper:
            print('You win this round!')
            user_score += 1
        elif computer_selection == rock:
            print('Computer wins this round!')
            computer_score += 1
    elif selection == rock:
        if computer_selection == rock:
            print('Draw!')
        elif computer_selection == scissors:
            print('You win this round!')
            user_score += 1
        elif computer_selection == paper:
            print('Computer wins this round!')
            computer_score += 1

print("\nGame over!")
if user_score > computer_score:
    print(f"You won! ({user_score} - {computer_score})")
elif user_score < computer_score:
    print(f"Computer won! ({computer_score} - {user_score})")
else:
    print(f"It's a tie! ({user_score} - {computer_score})")
