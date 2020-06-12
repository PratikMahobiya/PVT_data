#include <stdio.h>
int main()
{
	int x;
	printf("enter a no.");
	scanf("%d",&x);
	void rnum();
	rnum(x);
}
void rnum(int num)
{
	int r=0;
	while (num>0)		//513
	{
		r=(num%10)+10*r; //3+0=3 1+30=31  5+310=315
		//rv=rv*10+r;
		num=num/10;
	}
	printf("%d",r);
}