#include<stdio.h>
#include<conio.h>
int main()
{
	int rows,i,j,k;
	printf("enter the number of rows : ");
	scanf("%d",&rows);
	for(i=1;i<=rows;i++)
	{
		for(j=1;j<=rows-i;j++)
		{
			printf("$");
		}
		for(k=1;k<=i;k++)
		{
			printf(" *");
		}
		printf("\n");
	}
	printf("\n");
	return 0;
}