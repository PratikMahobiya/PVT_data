#include<iostream>
using namespace std;
class Test
{
	private:
		int a,b;
	public:
		Test()
		{
			a=10;
			b=20;
			cout<<a+b<<endl;
		}
		Test(int x, int y)
		{
			cout<<x+y;
		}
		
};
main()
{
	Test t;
	Test t2(100,200);
}