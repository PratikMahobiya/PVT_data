#include <stdio.h>
int main()
{
	int y=10;
	int *ptr;
	ptr=&y;
	printf("%d\n",y);
	printf("%d\n",ptr*2);
	printf("%d\n",*ptr);
	printf("%d",sizeof(*ptr));
}