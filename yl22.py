import random

while True:
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    user_choice = input('make a choice (1 - rock, 2 - paper, 3 - scissors): ')

    print('your choice was ', user_choice)
    print('computer choice was', computer_choice)

    if user_choice == 1 and computer_choice == 'scissors' or user_choice == 2 and computer_choice == 'rock' or user_choice == 3 and computer_choice == 'paper':
        print('you win')
    elif user_choice == computer_choice:
        print('draw')
    else:
        print('computer wins')

    print()