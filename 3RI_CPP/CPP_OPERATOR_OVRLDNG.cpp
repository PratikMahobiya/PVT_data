// All operator can be overloaded in cpp except :-
// 1. scoperesolution operator(::)
// 2. member func (*,.*)
// 3. sizeof(), conditional operator.

#include<iostream>
using namespace std;
class Test
{
	private:
		int x,y;
	public:
		void add(int a,int b)
		{
			x=a;
			y=b;
		}
		void display()
		{
			cout<<x<<" and "<<y;
		}
		Test operator +(Test t)
		{
			Test t3;
			t3.x=x+t.x;
			t3.y=y+t.y;
			return (t3);
		}
		
};
main()
{
	Test t,t1,t2;
	t.add(10,20);
	t1.add(100,200);
	t2=t+t1;
	t2.display();
}