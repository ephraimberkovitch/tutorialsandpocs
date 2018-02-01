#include <stdio.h>
#include "cs50.h"

int main()
{
    int height = -1;
    do 
    {
        printf("Height: ");
        height = get_int();
    }
    while (height<0||height>23);
    for (int i=0;i<height;i++)
    {
        for (int j=0;j<height-i-1;j++)
        {
            printf(" ");
        }
        for (int j=0;j<i+2;j++)
        {
            printf("#");
        }
        printf("\n");
    }
}