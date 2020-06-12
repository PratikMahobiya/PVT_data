#include<stdio.h>
void main()
{
	FILE *fptr;
	char str[20];
	int x;
	fptr=fopen("test.txt","r");
	if (fptr==NULL)
		puts("Can't open a file...........!!!");
	else
	{
		str=fread(str,1,sizeof(str),fptr);
		printf("%s",str);
	}
	fclose(fptr);
}