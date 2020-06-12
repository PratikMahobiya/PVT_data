#include<stdio.h>
void main()
{
	FILE *fptr;
	char str[]="c is programming language";
	int x;
	fptr=fopen("test.txt","w");
	if (fptr==NULL)
		puts("Can't open a file...........!!!");
	else
	{
		fwrite(str,1,sizeof(str),fptr);
	}
	fclose(fptr);
}