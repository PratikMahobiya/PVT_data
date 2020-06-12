#include<stdio.h>
int main()
{
	int x=3,z;
	z=++x * ++x + ++x;//3-111=-108 // x=x+1//3=4
	printf("%d %d",z,x);
	//++x;
	//printf("%d",x);
}