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
			cout<<" x is "<<x;
		}
		Test operator ++(int)
		{
			Test t;
			t.x=x++;
			return (t);
		}
		
};
main()
{
	Test t1;
	t1.setdata();
	t1.display();
	t1++;
	t1.display();
}