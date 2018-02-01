#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main()
{
    string full_name = get_string();
    int len = strlen(full_name);
    for (int i=0;i<len;i++)
    {
        if (i==0||full_name[i-1]==' ')
            printf("%c",toupper(full_name[i]));
    }
    printf("\n");
}