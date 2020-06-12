#include<stdio.h>
struct student
{
	int roll_no; //4
	char name[20];
	float per;
};
void display(struct student);
void main()
{
	struct student s={123,"pratik",86.478};
	display(s);
}
void  display(struct student var)
{
	puts("\n\n-------------WELCOME TO THE S_POINTER-------------");
	puts("-------------CHALIYE SURU KARTE HAI------------\n");
	printf("ROLL_NO:- \t%d\n",var.roll_no);
	printf("NAME:- \t\t%s\n",var.name);
	printf("PERCENTAGE:- \t%.2f\n",var.per);
	puts("\n-------- THE END ---------\n\n");
}