#include<stdio.h>
int main()
{
	int x,y,z;
	printf("Enter two numbers");
	scanf("%d %d",&x,&y);
	(x>y)? x++:y++; 
	z=x+y;
	printf("value of x is:-%d y is:-%d z is :-%d",x,y,z);
}