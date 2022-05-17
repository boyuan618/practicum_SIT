#include <stdio.h>
#include <string.h>

int main() {
    char *a = "abcdef"; 
    char b[7]; 
    strcpy(b, a); 
    for (int i = 0; i < 3; i++) 
        b[i] = b[i] + 1; 
    b[3] = '\0';


    printf("%c", a[0]);
    printf("\n");
    printf("%c", b[0]);
    printf("\n");
    printf("%c", b[4]);
    printf("\n");
    printf("%lu", strlen(a));
    printf("\n");
    printf("%lu", strlen(b));
    printf("\n");
    printf("%d", strcmp(a,b));


    return 0;
}