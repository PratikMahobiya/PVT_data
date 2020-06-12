#include<stdio.h>
void main()
{
	FILE *fptr;
	long pptr;
	char str2[50],str3[15];
	
	
	fptr=fopen("test.txt","r+");
	if(fptr==NULL)
		puts("Cant open");
	else
	{
		//reading
		pptr=ftell(fptr);
		printf("%ld is postion of ptr\n",pptr);
		fgets(str2,50,fptr);
		printf("before: %s\n",str2);
		pptr=ftell(fptr);
		printf("%ld is postion of ptr\n",pptr);
		
		//writing
		rewind(fptr);
		pptr=ftell(fptr);
		printf("%ld is postion of ptr\n",pptr);
		fseek(fptr,2,0);
		fputs("language",fptr);
		
		//again reading
		pptr=ftell(fptr);
		printf("%ld is postion of ptr\n",pptr);
		rewind(fptr);
		pptr=ftell(fptr);
		printf("%ld is postion of ptr\n",pptr);
		fgets(str3,15,fptr);
		printf("after: %s\n",str3);
	}
	fclose(fptr);
}