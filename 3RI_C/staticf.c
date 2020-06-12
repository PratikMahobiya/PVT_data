#include <stdio.h>
static int fun();
int main()
{
	int x,y;
	x=fun();
	printf("%d\n",x);
	y=fun();
	printf("%d\n",y);
}
static int fun()
{
	int x=1;
	x++;
	return x;
	
}