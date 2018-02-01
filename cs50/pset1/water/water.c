#include <stdio.h>
#include "cs50.h"

int main() 
{
    printf("Minutes: ");
    int minutes = get_int();
    int water = 12*minutes;
    printf("Water: %d\n",water);
}