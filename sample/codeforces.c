#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    printf("%s", (n % 2 || n == 2 ? "NO" : "YES"));
}