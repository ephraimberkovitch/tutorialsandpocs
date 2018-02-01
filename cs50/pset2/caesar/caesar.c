#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <cs50.h>

int main(int argc,string argv[])
{
    if (argc!=2)
    {
        printf("USAGE: ./caesar <numeric_key>\n");
        return 1;
    }
    int key = atoi(argv[1]);
    key = key % 26;
    printf("plaintext: ");
    string plain_text = get_string();
    printf("ciphertext: ");
    for (int i=0, n=strlen(plain_text);i<n;i++)
    {
        char p = plain_text[i];
        if (!isalpha(p))
            printf("%c",p);
        else
        {
            int c = p + key;
            if ((p>='a'&&p<='z'&&c>'z')||(p>='A'&&p<='Z'&&c>'Z'))
                c -= 26;
            printf("%c",c);
        }
    }
    printf("\n");
    return 0;
}