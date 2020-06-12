#include<stdio.h>
struct student
{
	int roll_no; 
	char name[20];
	float per;
};
void main()
{
	struct student *sptr,s={123,"pratik",86.478};
	puts("\n\n-------------WELCOME TO THE S_POINTER-----");
	puts("-------------CHALIYE SURU KARTE HAI------------\n");
	
	sptr=&s;
	
	printf("ROLL_NO:- \t%d\n",sptr->roll_no);
	printf("NAME:- \t%s\n",sptr->name);
	printf("PERCENTAGE:- \t%.2f\n",sptr->per);
	puts("\n-------- THE END ---------\n\n");
}