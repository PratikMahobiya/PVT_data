#include <stdio.h>
int main()
{
	void fact();
	fact();
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