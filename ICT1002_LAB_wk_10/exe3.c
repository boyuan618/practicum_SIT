#include <stdio.h>
#include <string.h>

typedef struct INTL_MONEY_VALUE {
    float value;
    char currency[4];
} Money;


typedef struct INTL_MONEY_VALUE_PTR {
    Money *Ptr;
} MoneyPtr;


int main() {
    Money test, test2;
    MoneyPtr testPtr;



    test.value = 192.66;
    strcpy(test.currency, "SGD");
    testPtr.Ptr = &test;
    test2 = *testPtr.Ptr;

    printf("%f", test.value);
    printf("\n");
    printf("%s", test.currency);
    printf("\n");

    printf("%f", test2.value);
    printf("\n");
    printf("%s", test2.currency);
    printf("\n");



    return 0;
}