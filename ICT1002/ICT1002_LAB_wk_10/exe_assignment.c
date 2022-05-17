#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

#define MAX_LETTERS 12
#define MAX_GUESSES 7

char input[MAX_LETTERS + 1];
char word[MAX_LETTERS + 1];
char guess[MAX_LETTERS + 1];
char current_guess;
int guesses_left = MAX_GUESSES;
bool success = false, input_valid = false, letter_in = false;



int main() {
    
    while (!input_valid) {
        /*Clearing the arrays*/
        memset(input, 0, MAX_LETTERS + 1);
        memset(word, 0, MAX_LETTERS + 1);
        memset(guess, 0, MAX_LETTERS + 1);

        /* Inputting the word to be guessed */
        printf("Player 1, enter a word of no more than %d letters:\n", MAX_LETTERS);
        fgets(input, MAX_LETTERS + 1, stdin);

        /*Validating the input*/
        for (int i=0;i<strlen(input) - 1;i++) {
            if (isalpha(input[i])) {
                word[i] = tolower(input[i]);
                guess[i] = '_';
                input_valid = true;
            } else {
                printf("Sorry, the word must contain only English letters.\n");
                input_valid = false;
                break;
            }
        }
        
    }
    
    while (!success && guesses_left > 0) {
        letter_in = false; //Resetting at start of each loop

        printf("Player 2 has so far guessed:");
        for (int i=0; i<strlen(guess);i++) {
          printf(" "); //To fufil the sample test case of no space after last underscore
          printf("%c", guess[i]);
        }

        if (strcmp(word, guess) == 0) {
            success = true;
            break;
        }

        printf("\nPlayer 2, you have %d guesses remaining. Enter your next guess:\n", guesses_left);
        current_guess = getchar();
        if (isalpha(current_guess)) {
            current_guess = tolower(current_guess);
        }

        getchar(); //Get the Enter after the character

        for (int i=0; i<strlen(word);i++) {
            if (word[i] == current_guess) {
                guess[i] = current_guess;
                letter_in = true;
            }
        }

        if(!letter_in) {
            guesses_left--;
        }
    }

    if (success) {
        printf("\nPlayer 2 wins.\n");
    } else {
        printf("Player 1 wins.\n");
    }

    return 0;
}