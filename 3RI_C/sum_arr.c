#include<stdio.h>
int main()
{
	int r1,r2,c1,c2;
	printf("Enter the rows and cols of 1st matrix\n");
	scanf("%d%d",&r1,&c1);
	printf("Enter the rows and cols of 2nd matrix\n");
	scanf("%d%d",&r2,&c2);
	if(r1==r2 && c1==c2)
	{	
		int a1[r1][c1];
		int a2[r2][c2];
		printf("Enter 1st matrix elements\n");
		for (int i=0;i<r1;i++)
		{
			for (int j=0;j<c1;j++)
			{
				printf("a1[%d][%d]:-",i,j);
				scanf("%d",&a1[i][j]);
			}
		}
		printf("---------------\n");
		printf("Enter 2nd matrix elements\n");
		for (int i=0;i<r2;i++)
		{
			for (int j=0;j<c2;j++)
			{
				printf("a2[%d][%d]:-",i,j);
				scanf("%d",&a2[i][j]);
			}
		}
		puts("sum is :-----------\n");
		for (int i=0;i<r1;i++)
		{
			for (int j=0;j<c1;j++)
			{
				int x;
				x= a1[i][j]+a2[i][j];
				printf("%d+%d:-%d\t",a1[i][j],a2[i][j],x);
			}
			printf("\n");
		}
	}
	else
		printf("\nSorry the rows and cols  of matrix are not same..!!!\n");
}