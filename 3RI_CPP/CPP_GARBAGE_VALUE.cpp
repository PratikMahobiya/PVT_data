#include<iostream>
using namespace std;
class Test
{
	public:
		int x,y;
	void print()
	{
		int res;
		cout<<x<<endl<<y<<endl;
		cout<<res<<endl;
	}
};
main()
{
	Test t,t1,t2;
	t.print();
	t1.print();
	t2.print();
}