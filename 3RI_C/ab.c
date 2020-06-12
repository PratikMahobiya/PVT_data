#include<stdio.h>
int main()
{
	int x;
	
	printf("enter a number");
	scanf("%d",&x);
	switch (x)
	{
		case 1 :
		{
			printf("case : 1" );
			break;
		}
		case 2 :
		{
			printf("case : 2" );
			break;
		}
		case 3 :
		{
			printf("case : 3" );
			break;
		}
		default :
		{
			printf("chal nikl :");
			break;
		}
	}
}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	if (x==1)
		printf("x=1");
	else if (x==2)
		printf("x=2");
	else if (x==4)
		printf("x=3");
	else
		printf("sorry");
}