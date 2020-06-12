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
		void setdata()
		{
			cout<<"enter x:-";
			cin>>x;
		}
		void display()
		{
			cout<<x<<" and "<<y;
		}
		Test operator ==(Test t)
		{
			if (x==t.x)
				cout<<"is equal";
			else
				cout<<"not equal";
		}
		
};
main()
{
	Test t1,t2;
	t1.setdata();
	t2.setdata();
	t1==t2;
	
	
}