#include<stdio.h>
int main()
{
	int n,m,result;
	printf("Enter the sixe of 1st array\n");
	scanf("%d",&n);
	printf("Enter the sixe of 2nd array\n");
	scanf("%d",&m);
	int a[n],a1[m];
	printf("Enter Values of 1st Array:---------");
	for (int i=0;i<n;i++)
	{
		printf("Enter the a[%d]:-",i);
		scanf("%d",&a[i]);
	}
	printf("Enter Values of 2nd Array:---------");
	for (int i=0;i<n;i++)
	{
		printf("Enter the a1[%d]:-",i);
		scanf("%d",&a1[i]);
	}
	printf("\nThe values are:---------VALUE--------\n");
	for (int j=0;j<n;j++)
	{
		printf("1st Array of a[%d]:- %d\t 2nd Array of a1[i]:- %d\n",j,j,a[j],a1[j]);
	}
	
}