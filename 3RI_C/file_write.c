#include<stdio.h>
void main()
{
	FILE *fptr,*fptr1;
	char str[30];
	char ch;
	fptr=fopen("C:/Users/Mahobiya_Mension/Desktop/pat.c","r");
	fptr1=fopen("test.txt","w+");
	if (fptr==NULL && fptr1==NULL)
		puts("Can't open a file...........!!!");
	else
	{
		ch=fgetc(fptr);
		while (ch!=EOF)
		{
			fputc(ch,fptr1);
			ch=fgetc(fptr);
		}
		while((fgets(str,30,fptr1))!=NULL)
		{
			printf("%s",str);
		}
	}
	fclose(fptr);
	fclose(fptr1);
}