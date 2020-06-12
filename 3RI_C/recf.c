#include <stdio.h>
int main()
{
	int a=4,x,y;
	int fact();
	x=fact(a);
	y=fact1(a);
	printf("fact is : %d",x);
}

int fact(int a)
{
	if (a==1)
		return 1;
	else
		return a*fact(a-1);
}

int fact1(int x)
{
	int fact=1;
	for(int i=1; i<=x;i++)
	{
		fact= fact*i;
	}
	return fact;
}