#include <stdio.h>
int main()
{
	register int sum=0,i;
	int x;
	puts("enter number");
	scanf("%d",&x);
	for ( i=1;i<=x;i++)
	{
		sum+=i;
	}
	printf("\nsum is %d",sum);
}
