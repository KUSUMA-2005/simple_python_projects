import random
while True:
    user_action=input("Enter Your Choice(rock, paper, scissors)")
    possible_actions=["rock","paper","scissor"]
    computer_action=random.choice(possible_actions)
    print(f"\nYou Chose {user_action}, computer chose {computer_action}.\n")
    if user_action==computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action=='rock':
        if computer_action=='scissor':
             print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action=='scissor':
            print("Scissors cuts paper! You lose!")
        else:
            print("Paper covers rock! You win.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break