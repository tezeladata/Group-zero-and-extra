#include <stdio.h>

#define MAX_CHAR 256

int main() {
    int c;
    int char_freq[MAX_CHAR] = {0};

    while((c=getchar()) != EOF){
        if (c >= 0 && c < MAX_CHAR){
            char_freq[c]++;
        }
    }

    printf("\nCharacter frequency histogram\n");
    for (int i = 0; i < MAX_CHAR; i++){
        if (char_freq[i] > 0) {
            // Printable
            if (i >= 32 && i <= 126){
                printf("\n%c ", i);
            } else { // Non-printable
                printf("\n%d ", c);
            }

            // * for each occurence
            for (int j = 0; j < char_freq[i]; j++){
                printf("*");
            }

            printf("\n");
        }
    }

    return 0;
}
