#include<stdio.h>
int main()
{
	int x;
	int *ptr,**ptr1;
	x=10;
	ptr=&x;
	ptr1=&ptr;
	
	printf("%d \n",x);//10
	printf("%d \n",*ptr);//10
	printf("%d \n",**ptr1);//10
}