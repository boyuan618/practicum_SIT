#include <stdio.h>
#include <stdbool.h>


#define TOTAL_GUESSES 10
#define HIGHEST_NUMBER 1000
#define LOWEST_NUMBER 1

int number, guess, guess_left=TOTAL_GUESSES;
bool in_range = false, success = false;

int main () {
    while (!in_range) {
        printf("Player 1, enter a number between %d and %d: ", LOWEST_NUMBER, HIGHEST_NUMBER);
        scanf("%d", &number);
        if (LOWEST_NUMBER<=number && number<=HIGHEST_NUMBER) {
            in_range = true;
        } else {
            printf("That number is out of range.\n");
        };
    };

    while (!success && guess_left) {
        printf("Player 2, you have %d guesses remaining.\n", guess_left);
        printf("Enter your guess: ");
        scanf("%d", &guess);

        if (guess == number) {
            success = true;
            printf("Player 2 wins.");
            return 0;
        } else if (guess < number) {
            printf("Too low.\n");
        } else {
            printf("Too high.\n");
        }

        guess_left -= 1;
    }
    printf("Player 1 wins.");

    return 0;
};