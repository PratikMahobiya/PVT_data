#include <stdio.h>
int main()
{
	int x,i,y;
	printf("Enter a Number:-");
	scanf("%d",&x);
	int prime();
	y=prime(x);
	if (y==2)
		printf("\n%d is prime number",x);
	else
		printf("\n%d Not Prime Number",x);
}
int prime(int x)
{
	int i,count=0;
	for (int i=1;i<=x;i++)
	{
		if(x%i==0)
			count++;
	}
	return count;
}

