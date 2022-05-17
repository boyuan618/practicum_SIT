#include <stdio.h>

int a = -1, b=2;
float x = 0.1;
float y = 1.5;
char c = 'p';

int main() {
    //part a
    printf("%d\n", a/b);
    printf("%d\n", a*b);
    printf("%d\n", (b*3)%4);
    printf("%f\n", x*a);
    printf("%f\n", x*y);
    printf("%f\n", y/x);
    printf("%d\n", (int)c-3);

    printf("\n");
    //part b
    printf("%4d", a);
    printf("%04d", b);
    printf("%x", b);
    printf("%.2f", y);
    printf("%10.1f", x);
    printf("c=\t%c", c);




    return 0;
}