#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <cs50.h>

int get_next_key_num(string key)
{
    static int current_key_index = -1;
    
    current_key_index++;
    if (current_key_index>strlen(key)-1)
        current_key_index = 0;

    int current_key = key[current_key_index];
    int current_key_num = 0;
    
    if (current_key>='a'&&current_key<='z')
        current_key_num = current_key-'a';
    else if (current_key>='A'&&current_key<='Z')
        current_key_num = current_key-'A';

    return current_key_num;
}

int main(int argc,string argv[])
{
    if (argc!=2)
    {
        printf("USAGE: ./vigenere <alphabetical_word_key>\n");
        return 1;
    }
    string key = argv[1];
    int len = strlen(key);
    for (int i=0;i<len;i++)
    {
        if (!isalpha(key[i]))
        {
            printf("USAGE: ./vigenere <alphabetical_word_key>\n");
            return 1;
        }
    }
    
    printf("plaintext: ");
    string plain_text = get_string();
    printf("ciphertext: ");
    for (int i=0,n=strlen(plain_text);i<n;i++)
    {
        char p = plain_text[i];
        if (!isalpha(p))
            printf("%c",p);
        else
        {
            int c = p + get_next_key_num(key);
            if ((p>='a'&&p<='z'&&c>'z')||(p>='A'&&p<='Z'&&c>'Z'))
                c -= 26;
            printf("%c",c);
        }
        
    }
    
    printf("\n");
    return 0;
}