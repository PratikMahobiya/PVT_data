#include<stdio.h>
void swap();
void sw();
int main()
{
	int x=10,y=20;
	printf("%d,%d\n",x,y);
	swap(&x,&y);
	sw(x,y);
}
void  swap(int *x,int *y)  
{
	int t;
	t=*x;
	*x=*y;
	*y=t;
	printf("%d,%d\n",*x,*y);
}
void  sw(int x,int y)
{
	x=x+y;
	y=x-y;
	x=x-y;
	printf("%d,%d",x,y);
}