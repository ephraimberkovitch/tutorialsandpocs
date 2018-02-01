#include <stdio.h>
#include <math.h>
#include "cs50.h"

int main()
{
    printf("O hai! ");
    float input;
    do
    {
        printf("How much change is owed?\n");
        input = get_float();
    }
    while (input<0);
    int num = (int)round(100.0*input);
    int coins[4] = {25,10,5,1};
    int count = 0;
    for(int i=0;i<4;i++)
    {
        int times = num/coins[i];
        count += times;
        num -= times*coins[i];
    }
    printf("%d\n",count);
}