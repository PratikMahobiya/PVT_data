#include <stdio.h>
int main()
{
	int x=10;
	void fun();
	fun();
}
void fun()
{
	extern int n;
	n++;
	printf("%d \n",n);
}