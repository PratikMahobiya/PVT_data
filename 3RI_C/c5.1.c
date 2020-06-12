#include<stdio.h>
int main()
{
	int n=3,x;
	if(n<5)
	{
		printf("%d/n",n);
 		x=++n;
		printf("%d/n%d",x,n);
	}
	else
		printf("sorry");
}