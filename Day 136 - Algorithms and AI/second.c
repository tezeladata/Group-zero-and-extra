#include <stdio.h>

int main() {
    int c, lastChar;

    lastChar = 0;

    while ((c = getchar()) != EOF) {
        if (c != ' ') {
            putchar(c);
        } else if (lastChar != ' ') {
            putchar(c);
        }
        lastChar = c;
    }

    return 0;
}
