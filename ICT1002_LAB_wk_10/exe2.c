#include <stdio.h>


long value1 = 200000;
long value2, *lPtr;

int main() {
    lPtr = &value1;
    printf("%ld", *lPtr);
    printf("\n");

    value2 = *lPtr;
    printf("%ld", value2);
    printf("\n");
    printf("%p", &value1);
    printf("\n");
    printf("%p", &lPtr);
    /*lPtr and value1 do not have the same address*/




    return 0;
}