#include<stdio.h>
struct student
{
	int roll_no; 
	char name[20];
	float per;
};
void main()
{
	struct student s[2];  //as same as :-  int x[2];
	puts("\n\n-------------WELCOME TO THE JUMANJI--------------");
	puts("-------------CHALIYE SURU KARTE HAI------------\n");
	
	//writing
	for (int i=0;i<2;i++)
	{
		printf("%d'student roll_no:- ",i+1);
		scanf("%d",&s[i].roll_no);
		printf("%d'Student name:- ",i+1);
		scanf("%s",s[i].name);
		printf("%s's Percentage:- ",s[i].name);
		scanf("%f",&s[i].per);
		if(i<1)
			printf("\n\nEnter Next Student Details...!!!\n");
		else
			puts("\n\n------------:The Details Are:--------\n");
	}
	//reading
	for (int i=0;i<2;i++)
	{
		printf("\nDETAIL of %s...!!!\n",s[i].name);
		printf("%d student roll_no:- \t%d\n",i+1,s[i].roll_no);
		printf("%d student name:- \t%s\n",i+1,s[i].name);
		printf("%s percentage:- \t%.2f\n\n\n",s[i].name,s[i].per);
	}
}