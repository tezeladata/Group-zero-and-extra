#include <stdio.h>

int main ()
{
    int c, nl, nb, nt;

    nl = 0;
    nb = 0;
    nt = 0;

    while ((c = getchar()) != EOF)
    {
        if (c == '\n')
           ++nl;
        if (c == '\t')
           ++nt;
        if (c == ' ')
           ++nb;
    }

    printf("\nNew line Count: %d\nTabs count: %d\nBlanks count: %d\n", nl, nt, nb);

    return 0;
}
