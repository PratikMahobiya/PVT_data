#include <stdio.h>
static int n=1;
void even();
void odd();

int main()
{
	odd();
}
void odd()
{
		while(n<10)
	{
		printf("%d ",n+1);
		n++;
		even();
	}
}
void even()
{
		while(n<10)
	{
		printf("%d ",n-1);
		n++;
		odd();
	}
}