#include<stdio.h>
 
int main()
{
	char str[50],ch;
	int k;
	
	printf("Enter a string: ");
	scanf("%s",&str);

	printf("Enter key: ");
	scanf("%d",&k);
	
	for(int i=0; str[i] != '\0'; i++)
	{
		ch = str[i];
		
		if(ch  >= 'a' && ch <= 'z')
		{
			ch = ch + k;
			
			if(ch > 'z')
			{
				ch=ch-'z'+'a'- 1;
			}
			
			str[i] = ch; 
		}

		else if(ch >= 'A' && ch <= 'Z')
		{
			ch = ch+k;
			
			if(ch > 'Z')
			{
				ch = ch-'Z'+'A'-1;
			}
			
			str[i] = ch;  
		}
	}
	
	printf("Cipher text is: %s",str);
	
	return 0;
}