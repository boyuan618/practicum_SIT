#include <stdio.h>

float weight, height;
const char * range = "";

int main() {
    printf("Enter your weight in kilograms: ");
    scanf("%f", &weight);
    printf("Enter your weight in metres: ");
    scanf("%f", &height);

    float bmi = weight / (height*height);

    if (bmi < 18.5) {
        range = "underweight";
    } else if (bmi < 25.0) {
        range = "normal";
    } else if (bmi < 30.0) {
        range = "overweight";
    } else {
        range = "obese";
    }

    printf("Your BMI is %.1f. That is within the %s range.", bmi,range);
    return 0;
}