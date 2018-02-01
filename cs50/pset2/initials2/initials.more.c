#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main()
{
    string full_name = get_string();
    int len = strlen(full_name);
    int i = 0;
    while (i<len)
    {
        while (i<len&&full_name[i]==' ')
            i++;
        if (i<len)
            printf("%c",toupper(full_name[i]));
        while (i<len&&full_name[i]!=' ')
            i++;
    }
    printf("\n");
}