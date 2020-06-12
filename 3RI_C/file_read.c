#include<stdio.h>
void main()
{
	FILE *fptr;
	char str[30];
	int x;
	fptr=fopen("test.txt","r");
	if (fptr==NULL)
		puts("Can't open a file...........!!!");
	else
	{
		while((fgets(str,30,fptr))!=NULL)
		{
			printf("%s",str);
		}
	}
	fclose(fptr);
}