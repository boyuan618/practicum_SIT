#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX_SIZE 255

char sentence[MAX_SIZE + 2];
int len,start,end = 0;


int main() {

    printf("%s", "Enter a sentence, up to 255 characters: ");
    fgets(sentence, MAX_SIZE + 2, stdin);
    for (int i=0;i<strlen(sentence);i++) {
        if (isalpha(sentence[i])) {
            len++;
            end++;
        } else if (len == 0) {
            start++;
            end++;
        } else {
            for (int j=start;j<end;j++) {
                printf("%c",sentence[j]);
            }
            printf(" %d",len);
            printf("\n");
            len = 0;
            end++;
            start = end;
        }
    }


    return 0;
}

 
