#include <stdio.h>

#define MAX_WORD_LENGTH 20
#define IN 1
#define OUT 0

int main() {
    int c, i, j, state, word_length;
    int word_lengths[MAX_WORD_LENGTH + 1] = {0};
    int max_word_count = 0;

    state = OUT;
    word_length = 0;

    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\n' || c == '\t') {
            if (state == IN) {
                if (word_length <= MAX_WORD_LENGTH) {
                    word_lengths[word_length]++;
                    if (word_lengths[word_length] > max_word_count) {
                        max_word_count = word_lengths[word_length];
                    }
                }
                word_length = 0;
            }
            state = OUT;
        } else {
            if (state == OUT) {
                state = IN;
                word_length = 1;
            } else {
                word_length++;
            }
        }
    }

    printf("\nVertical Histogram of Word Lengths\n");
    for (i = max_word_count; i > 0; i--) {
        for (j = 1; j <= MAX_WORD_LENGTH; j++) {
            if (word_lengths[j] >= i) {
                printf("  *  ");
            } else {
                printf("     ");
            }
        }
        printf("\n");
    }

    for (i = 1; i <= MAX_WORD_LENGTH; i++) {
        printf(" %3d ", i);
    }
    printf("\n");

    return 0;
}
