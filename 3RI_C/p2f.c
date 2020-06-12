#include<stdio.h>
int add(int x,int y);
int main()
{
	int x=10,y=2,z;
	int (*ptr)(int , int);
	ptr=&add;
	z=add(x,y);
	printf("z=: %d\n",z);
	printf("Ptr=: %d",ptr);
}
int add(int x,int y)
{
	return x+y;
}