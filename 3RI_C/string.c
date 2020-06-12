	#include<stdio.h>
	#include<string.h>
	int main()
	{
		char ch[10];
		int count=0;
		gets(ch);
		for (int i=0;ch[i] != '\0';i++)
		{
			count++;
		}
		puts(ch);
		printf("%d",count);
	}