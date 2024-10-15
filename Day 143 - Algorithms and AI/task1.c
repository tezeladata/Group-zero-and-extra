#include <stdio.h>

int get_temp(int celsius);

int main() {
    int temp = 0;
    char c;

    printf("Please enter your temperature number in celsius\n");

    while ((c = getchar()) != '\n'){
        if (c >= '0' && c <= '9') {
            temp = temp * 10 + (c - '0');
        } else {
            printf("Invalid input. Please enter only digits.\n");
            return 1;
        }
    }

    printf("\nYour temperature in fahrenheit is %d\n", get_temp(temp));

    return 0;
}

int get_temp(int celsius){
    return (celsius * 9/5) + 32;
}
