#include<stdio.h>
struct _3Ri 
{
	struct c_class
	{
		char name[20];
		int fees,paid_amt;
	}c[2];
	struct html
	{
		char name[20];
		int fees,paid_amt;
	}h[2];
}s;
void main()
{
	struct _3Ri s;
	int x;
	puts("Class of C or Html: 1 for C & 2 for Html:\n");
	scanf("%d",&x);
	if (x==1)
	{
		//writing in C class:-
		for (int i=0;i<2;i++)
		{
			printf("%d student Name:- \n",i+1);
			scanf("%s",s.c[i].name);
			printf("%d student Fees:- \n",i+1);
			scanf("%d",&s.c[i].fees);
			printf("%d student paid_amt:- \n",i+1);
			scanf("%d",&s.c[i].paid_amt);		
			printf("\n--!!--\n");
		}
		
		//reading
		puts("\n\n------------:The Details Of C classes are:--------\n");
		for (int i=0;i<2;i++)
		{
			printf("%d student name:- %s\n",i+1,s.c[i].name);
			printf("%s's fees:- %d\n",s.c[i].name,s.c[i].fees);
			printf("%s's Due_amount:- %d\n---\n\n",s.c[i].name,s.c[i].fees-s.c[i].paid_amt);
		}
	}
	else
	{
		//writing in Html class:-
		for (int i=0;i<2;i++)
		{
			printf("%d student Name:- \n",i+1);
			scanf("%s",s.h[i].name);
			printf("%d student Fees:- \n",i+1);
			scanf("%d",&s.h[i].fees);
			printf("%d student paid_amt:- \n",i+1);
			scanf("%d",&s.h[i].paid_amt);
			printf("\n--!!--\n");
		}
		
		//reading
		puts("\n\n------------:The Details Of Html classes are:--------\n");
		for (int i=0;i<2;i++)
		{
			printf("%d student name:- %s\n",i+1,s.h[i].name);
			printf("%s's fees:- %d\n",s.h[i].name,s.h[i].fees);
			printf("%s's Due_amount:- %d\n---\n\n",s.h[i].name,s.h[i].fees-s.h[i].paid_amt);
		}
	}
}