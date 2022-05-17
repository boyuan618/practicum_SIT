#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <regex.h>

#define MAX_SIZE 255

//Input variables
char sentence[MAX_SIZE + 2];
char pattern_input[MAX_SIZE + 2];
char pattern[MAX_SIZE + 2] = "";
char case_sensitive[1];

//Regex variables
regex_t regex;
regmatch_t match;
int result;

int main() {
    //Getting the inputs
    printf("%s", "Enter a sentence, up to 255 characters: ");
    fgets(sentence, MAX_SIZE + 2, stdin);

    printf("%s", "Enter a pattern, up to 255 characters: ");
    fgets(pattern_input, MAX_SIZE + 2, stdin);

    printf("%s", "Case sensitive: Y/N");
    printf("\n");
    scanf("%c", &case_sensitive[0]);

    //Lowering the case if not case sensitive
    if (strcmp(case_sensitive, "N") == 0) {
        for (int i=0; i<sentence[i]; i++) {
            sentence[i] = tolower(sentence[i]);
        }
    }
    //Swapping out _ to \s so that regex recognises whitespace
    for (int i=0;i<strlen(pattern_input);i++) {
      char character = pattern_input[i];
      if (character == '_') {
        strncat(pattern, "\\s", 2);
      } else {
        strncat(pattern, &character, 1);
      }
    }

    //Removing newline that causes many problems
    strtok(sentence, "\n");
    strtok(pattern, "\n");

    //Regex
    result = regcomp(&regex, pattern, 0);
    result = regexec(&regex, sentence, 1, &match, 0);
    if (result == 0) {
      printf("Matches at position %d.", match.rm_so);
    } else {
      printf("No match");
    }

    return 0;
}
