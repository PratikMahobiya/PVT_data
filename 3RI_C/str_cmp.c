#include<stdio.h>
#include<string.h>
int main()
{
	char ch[10],ch1[10];
	int len,count;
	gets(ch);
	gets(ch1);
	len=strlen(ch);
	for (int i=0;i <= len;i++)
	{
		if(ch[i]==ch1[i])
		{
			count=1;
		}
		else
		{
			count=0;
			break;
		}
		
	}
	if (count==1)
		printf("str is same\n");
	else
		printf("not same \n");
	
}