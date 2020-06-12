#include<stdio.h>
struct _3Ri 
{
	struct c_class
	{
		char name[20];
		int fees,paid_amt;
	}c;
	struct html
	{
		char name[20];
		int fees,paid_amt;
	}h;
}s;
void main()
{
	struct _3Ri *sptr;
	struct _3Ri s;
	struct c_class *cptr,c={"pratik", 5000, 200};
	cptr=&c;
	sptr=&s;
	printf("%d\n",cptr->fees);
	//------------------ ------------------NAI HUA RE--------------------BAD ME KRNA JARUR-----
}