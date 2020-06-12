#include <stdio.h>
int fun1();
int main()
{
	long int n;
	printf("enter a value");
	scanf("%ld",&n);
	printf("%ld",fun1(n));
}

int fun1(long int n)
{
	if(n==1)
		return 1;
	else
		return 1+fun1(n-1)*10;
}