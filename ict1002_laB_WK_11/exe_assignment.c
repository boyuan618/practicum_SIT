#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>

#define MAX_WORD_LENGTH 32


struct word_node { 
char word[MAX_WORD_LENGTH + 1];
struct word_node *next; 
}; 

typedef struct word_node WORD_NODE; 
typedef WORD_NODE *WORD_NODE_PTR;


void printList(WORD_NODE_PTR n)
{
    while (n != NULL) {
        printf("%s", n->word);
        n = n->next;
    }
}



int main() {
    WORD_NODE_PTR head = NULL;
    WORD_NODE_PTR curr = head;
    WORD_NODE_PTR prev = head;
    char curr_word[MAX_WORD_LENGTH + 1] = "";
    bool word_valid = true;
    bool word_inserted = false;


    while (strcmp(curr_word, "***\n") != 0){
        //resetting variables
        WORD_NODE *curr_node = malloc(sizeof(WORD_NODE));
        curr = head;
        prev = head;
        word_inserted = false;
        word_valid = true;
        
        printf("Please enter a word:\n");
        if (fgets(curr_word, MAX_WORD_LENGTH + 1, stdin) == NULL) {

            /*Error handling*/
            if (feof(stdin)) printf("End-of-file occurred");
            if (ferror(stdin)) {
                clearerr(stdin);
                printf("Input error occurred"); 
            }
            
            continue;
        }

        for (int i=0;i < strlen(curr_word) - 1;i++) {
            if (isalpha(curr_word[i]) || curr_word[i] == '\'' || curr_word[i] == '-'){
                curr_word[i] = tolower(curr_word[i]);
            } else if (strcmp(curr_word, "***\n") == 0) {
                word_valid = false;
                break;
            } else {
                printf("Sorry, the word must contain only English letters, apostrophes, and hyphens.\n");
                word_valid = false;
                break;
            }
        }
        if (!word_valid) {
            continue;
        }

        
        strcpy(curr_node->word, curr_word);
        curr_node->next = NULL;

        //Start of comparison
        if (head == NULL) {
            head = curr_node;
        } else {
            while (!word_inserted) {
              if (curr == NULL) { //At the end
                prev->next = curr_node;
                word_inserted = true;
              } else if (strcmp(curr_node->word, curr->word) < 0) { //the current word is smaller than then word in the current node
                if (prev == curr) {
                    curr_node->next = curr;
                    head = curr_node;
                } else {
                    prev->next = curr_node;
                    curr_node->next = curr;
                }
                word_inserted = true;
              } else {
                  prev = curr;
                  curr = curr->next;
              }
            }
        }
    }
    printf("All the entered words in order:\n");
    printList(head);


    return 0;
}