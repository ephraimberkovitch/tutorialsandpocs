#include <stdio.h>
#include "cs50.h"

int main()
{
    long long cc_num;
    do 
    {
        printf("Number: ");
        cc_num = get_long_long();    
    }
    while(cc_num<0);
    int position = 0;
    int sum_digits = 0;
    int digit = 0, prev_digit;
    int num_digits = 0;
    do
    {
        prev_digit = digit;
        digit = cc_num % 10;
        position++;
        if (position%2==1)
            sum_digits += digit;
        else
        {
            int digit2 = 2*digit;
            if (digit2<10)
                sum_digits += digit2;
            else
                sum_digits += 1+digit2%10;
        }
        cc_num = cc_num/10;
        num_digits++;
    }
    while (cc_num>0);
    
    if (sum_digits%10!=0)
        printf("INVALID\n");
    else
    {
        if (digit==3&&(prev_digit==4||prev_digit==7)&&num_digits==15)
            printf("AMEX\n");
        else if (digit==4&&(num_digits==13||num_digits==16))
            printf("VISA\n");
        else if (digit==5&&(prev_digit>0&&prev_digit<6)&&num_digits==16)
            printf("MASTERCARD\n");
        else
            printf("INVALID\n");
    }
}