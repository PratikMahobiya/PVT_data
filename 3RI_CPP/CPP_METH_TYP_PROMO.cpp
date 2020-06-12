#include<iostream>
using namespace std;
class Test
{
	private:
		int a,b;
	public:
		void add(int  a)
		{
			cout<<a<<endl;
		}
		void add(double x)
		{
			cout<<x;
		}
		
};
main()
{
	char ch='B';
	Test t;
	t.add(ch);
	
}