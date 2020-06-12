#include <stdio.h>
int fact();
int main()
{
	int x,y;
	puts("Enter a no.:- ");
	scanf("%d",&x);
	y=fact(x);
	printf("%d",y);
	return 0;
}
int fact(int x)
{
	if(x>0)
		return (x*fact(x-1));
	else
		return 1;
}