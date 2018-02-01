#define _XOPEN_SOURCE
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <cs50.h>

#define PASSWORD_CHARACTERS 53
#define SALT_CHARACTERS 64

//clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wshadow crack.c -lcrypt -lcs50 -lm -o crack

int main(int argc,string argv[])
{
    if (argc!=2)
    {
        printf("USAGE: crack <hashed_password>\n");
        return 1;
    }
    string hash = argv[1];
    
    char password_characters[PASSWORD_CHARACTERS];
    int password_characters_index = 0;
    password_characters[password_characters_index] = ' ';
    password_characters_index++;
    for (char c='a';c<='z';c++)
    {
        password_characters[password_characters_index] = c;
        password_characters_index++;
    }
    for (char c='A';c<='Z';c++)
    {
        password_characters[password_characters_index] = c;
        password_characters_index++;
    }
    
    //salt is a two-character string chosen from the set [a–zA–Z0–9./]
    char salt_characters[SALT_CHARACTERS];
    int salt_characters_index = 0;
    for (char c='a';c<='z';c++)
    {
        salt_characters[salt_characters_index] = c;
        salt_characters_index++;
    }
    for (char c='A';c<='Z';c++)
    {
        salt_characters[salt_characters_index] = c;
        salt_characters_index++;
    }
    for (char c='0';c<='9';c++)
    {
        salt_characters[salt_characters_index] = c;
        salt_characters_index++;
    }
    salt_characters[salt_characters_index] = '.';
    salt_characters[++salt_characters_index] = '/';
    int counter = 0;
    //printf("%s\t%s\n",password_characters,salt_characters);
    for (int d1=0;d1<PASSWORD_CHARACTERS;d1++)
        for (int d2=0;d2<PASSWORD_CHARACTERS;d2++)
            for (int d3=0;d3<PASSWORD_CHARACTERS;d3++)
                for (int d4=0;d4<PASSWORD_CHARACTERS;d4++)
                {
                    char pwd[5] = {' ',' ',' ',' ','\0'};
                    int pwd_index = 0;
                    if (password_characters[d1]!=' ')
                    {
                        pwd[pwd_index] = password_characters[d1];
                        pwd_index++;
                    }
                    if (password_characters[d2]!=' ') 
                    {
                        pwd[pwd_index] = password_characters[d2];
                        pwd_index++;
                    }
                    if (password_characters[d3]!=' ') 
                    {
                        pwd[pwd_index] = password_characters[d3];
                        pwd_index++;
                    }
                    if (password_characters[d4]!=' ')
                    {
                        pwd[pwd_index] = password_characters[d4];
                        pwd_index++;
                    }
                    if (pwd_index==0) //4 spaces - irrelevant; we are testing 1-4 characters in password
                        continue;
                    pwd[pwd_index] = '\0';
                    for (int s1=0;s1<SALT_CHARACTERS;s1++) 
                        for (int s2=0;s2<SALT_CHARACTERS;s2++)
                        {
                            char salt[3] = {' ',' ','\0'};
                            salt[0] = salt_characters[s1];
                            salt[1] = salt_characters[s2];
                            //printf("%s\t%s\n",pwd,salt);
                            string guess = crypt(pwd,salt);
                            counter++;
                            if (strcmp(guess,hash)==0)
                            {
                                printf("%s\n",pwd);
                                return 0;
                            }
                        }
                }
    printf("Not found\n");
    return 0;
}