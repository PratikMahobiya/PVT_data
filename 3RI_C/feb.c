#include <stdio.h>
int febo();
int main()
{
	int x,y;
	puts("Enter a no.:- ");
	scanf("%d",&x);
	y=febo(x);
	printf("%d",y);
	return 0;
}
int febo(int x)
{
	if(x>0)
		return (febo(x-1)+febo(x-2));
	else
		return 1;
}