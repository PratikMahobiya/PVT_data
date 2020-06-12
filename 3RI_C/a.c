#include <stdio.h>
int add();
int sub();
int mul();
int div();
int menu();


int main()
{
	menu();
	int a,x,y;
	printf("Enter your choice:- ");
	scanf("%d",&a);
	printf("Enter Two numbers");
	scanf("%d %d",&x,&y);
	
	switch(a)
	{
		case 1 :
			add(x,y);
			break;
		case 2 :
			sub(x,y);
			break;
		case 3 :
			mul(x,y);
			break;
		case 4:
			div(x,y);
			break;
		default:
			printf("Wrong Input");
			break;
	}
	return 0;
}
int menu()
{
	printf("Welcome...\n");
	printf("1: Addition\n");
	printf("2: Subtraction\n");
	printf("3: Multiplication\n");
	printf("4: Division\n");
}
int add(int a,int b)
{
	int c;
	c=a+b;
	printf("addition is %d\n",c);
}
int sub(int a,int b)
{
	int c;
	c=a-b;
	printf("addition is %d\n",c);
}
int mul(int a,int b)
{
	int c;
	c=a*b;
	printf("addition is %d\n",c);
}
int div(int a,int b)
{
	int c;
	c=a/b;
	printf("addition is %d\n",c);
}




































void fact()
{
	int fact=1,x;
	printf("enter a no.");
	scanf("%d",&x);
	for(int i=1;i<=x;i++)
	{
		fact=fact*i;
	}
	printf("fact is %d\n",fact);
}