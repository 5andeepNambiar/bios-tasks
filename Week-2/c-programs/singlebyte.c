#include<stdio.h>
#include<string.h>
void str_xor(char xor_string[],char k[])
{
    int len = strlen(xor_string);
    printf("\nCiphered String is: ");
    for (int i = 0; i < len; i++)
    {
        xor_string[i]=xor_string[i]^k[0];
        printf("%c", xor_string[i]);
    }
    
}

int main()
{
    char string[50],key[2];
    printf("Enter String: ");
    scanf("%s",&string);
    printf("Enter a single byte character: ");
    scanf("%s",&key);
    str_xor(string,key);
    return 0;
}