#include <stdio.h>

int main(void) {
    int n;

    while (scanf("%d", &n)) {
        if (n == 42) {
            break;
        }

        printf("%d\n", n);
    }
}