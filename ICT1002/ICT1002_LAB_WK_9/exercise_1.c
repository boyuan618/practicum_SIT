#include <stdio.h>


int main() {
    int a[4] = { -1, 2, 10, 7 }; 
    int b[4]; 
    for (int i = 0; i < 4; i++) {
        b[i] = a[3 - i];
    }


    printf("%d", a[3]);
    printf("\n");
    printf("%d", b[3]);
    printf("\n");
    printf("%d", b[a[1]]);



    return 0;
}