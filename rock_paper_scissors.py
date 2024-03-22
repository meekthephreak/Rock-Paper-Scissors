import random

possible_actions = ['rock', 'paper', 'scissors']
user_name = input('Enter your name: ')
print('Hi {}! Tyree would like you to test out his game!'.format(user_name))


def error_message():
    print('{} is not a valid choice!! You are stupid'.format(user_action))


while True:
    user_action = input('Enter a choice (rock, paper, scissors): ')
    computer_action = random.choice(possible_actions)
    print(f'\nYou chose {user_action}, computer chose {computer_action}\n')
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        continue
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            break
        else:
            print("Paper covers rock! You lose.")
            break
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            break
        else:
            print("Scissors cuts paper! You lose.")
            break
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            break
        else:
            print("Rock smashes scissors! You lose.")
            break
    elif user_action not in possible_actions:
        error_message()
        continue
