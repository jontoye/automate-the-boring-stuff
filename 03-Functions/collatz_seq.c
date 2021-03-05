#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int collatz(int number);

int main(void)
{
    int n;
    clock_t start, end;
    double duration;

    printf("Enter a number: ");
    scanf("%d", &n);

    while (n != 1)
        n = collatz(n);

    exit(EXIT_FAILURE);
}

int collatz(int number)
{
    int res;
    if (number % 2 == 0)
        res = number / 2;
    else
        res = 3 * number + 1;
    printf("%d\n", res);
    return res;
}