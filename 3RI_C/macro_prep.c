#include<stdio.h>
#define pi 3.14
#define class "hello"
int area(int);
int circ(int);
void circle()
{
	float radius;
	puts("Enter radius of circle");
	scanf("%f",&radius);
	printf("define class is ",class);
	area(radius);
	circ(radius);
}
int area(int radius)
{
	float area;
	area=radius*radius*pi;
	printf("area is %f\n",area);
}
int circ(int radius)
{
	float circ;
	circ=2*radius*pi;
	printf("circumference is %f\n",circ);
}