#include<stdio.h>
int main()
{
	int a[]={10,3,54,5,9,47,-8,6},max=a[0];
	for (int i=0;i<8;i++)
	{
		if (max<a[i])
		{
			max=a[i];
		}
	}
	printf("\nMax Of Arry is :- %d",max);
}