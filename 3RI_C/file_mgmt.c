#include<stdio.h>
void main()
{
	FILE *fptr;
	int x;
	fptr=fopen("str_.c","r");
	if (fptr!=NULL)
	{
		puts("OPENED SUCCESSFULLY");
		while ((x=fgetc(fptr))!=EOF)
		{
			printf("%c",x);
		}
	}
	else
		puts("Can't Open\n");
	
}