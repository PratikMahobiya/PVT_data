#include<iostream>
using namespace std;
class Test
{
	private:
		int a,b;
	public:
		void add(int  a, int b)
		{
			cout<<a+b<<endl;
		}
		void add(double x,double y)
		{
			cout<<x+y;
		}
		
};
main()
{
	Test t;
	t.add(10,56);
	t.add(12.4,35.789);
}