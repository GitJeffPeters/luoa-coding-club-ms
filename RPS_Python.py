
import random
import os

def get_user_choice():
    print("     Python")
    print("----------------\n")
    user_choice = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ")
    return user_choice.lower()

def get_computer_choice():
    choices = ['r', 'p', 's']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'r' and computer_choice == 's') or \
         (player_choice == 'p' and computer_choice == 'r') or \
         (player_choice == 's' and computer_choice == 'p'):
        return "You win this round!"
    else:
        return "Computer wins this round!"

def main():
    player_score = 0
    computer_score = 0

    while player_score < 5 and computer_score < 5:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        if computer_choice == 'r':
            computers_choice = "Rock"
        elif computer_choice == 'p':
            computers_choice = "Paper"
        elif computer_choice == 's':
            computers_choice = "Scissors"
            
        print("Computer chose:", computers_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "You win" in result:
            player_score += 1
        elif "Computer wins" in result:
            computer_score += 1

        print(f"Your Score: {player_score} | Computer Score: {computer_score}\n")
        os.system('timeout /t 2 > nul')
        os.system('cls')

    if player_score == 5:
        print("Congratulations! You are the overall winner!")
    else:
        print("Sorry, the computer is the overall winner. Better luck next time!")

if __name__ == "__main__":
    main()
