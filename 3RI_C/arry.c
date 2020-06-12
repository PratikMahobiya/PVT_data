#include<stdio.h>
int main()
{
	int n,result=0;
	printf("Enter the sixe of array\n");
	scanf("%d",&n);
	int a[n];
	
	for (int i=0;i<n;i++)
	{
		printf("Enter the a[%d]:-",i);
		scanf("%d",&a[i]);
	}
	printf("\nThe values are:---------VALUE--------\n");
	for (int j=0;j<n;j++)
	{
	printf("Array if a[%d]:- %d\n",j,a[j]);
	}
	printf("\nSum of array is:--------SUM--------\n");
	for (int i=0;i<n;i++)
	{
		result += a[i];
	}
	printf("sum if Array is :- %d",result);
}