#include <iostream>
#include <ctime>
#include <cstdlib>
#include <chrono>
#include <thread>


using namespace std;

int main() {
    int playerScore = 0;
    int computerScore = 0;
    char choices[] = { 'r', 'p', 's' };
    string computersChoice;

    srand(time(0)); // Seed for random number generation

    while (playerScore < 5 && computerScore < 5) {
        system("cls");
        cout << "      C++" << endl;
        cout << "----------------" << endl << endl;
        cout << "Enter your choice (r for Rock, p for Paper, s for Scissors): ";
        char playerChoice;
        cin >> playerChoice;

        // Generate random computer choice
        char computerChoice = choices[rand() % 3];
        switch (computerChoice) {
            case 'r':
                computersChoice = "Rock";
                break;
            case 's':
                computersChoice = "Scissors";
                break;
            case 'p':
                computersChoice = "Paper";
                break;
        }
        cout << "Computer chose: " << computersChoice << endl;

        // Determine winner
        if (playerChoice == computerChoice) {
            cout << "It's a tie!" << endl;
        }
        else if ((playerChoice == 'r' && computerChoice == 's') ||
            (playerChoice == 'p' && computerChoice == 'r') ||
            (playerChoice == 's' && computerChoice == 'p')) {
            cout << "You win this round!" << endl;
            playerScore++;
        }
        else {
            cout << "Computer wins this round!" << endl;
            computerScore++;
        }

        cout << "Your Score: " << playerScore << " | Computer Score: " << computerScore << endl << endl;
        system("timeout 2 > nul");
    }

    // Determine overall winner
    if (playerScore == 5) {
        cout << "Congratulations! You are the overall winner!" << endl;
    }
    else {
        cout << "Sorry, the computer is the overall winner. Better luck next time!" << endl;
    }

    return 0;
}
