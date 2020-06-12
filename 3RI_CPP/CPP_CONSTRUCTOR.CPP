#include<iostream>
using namespace std;
class Test
{
	public:
		Test()
		{
			cout<<"0- args = Default Constructor"<<endl;
		}
		Test(int a)
		{
			cout<<"1- args = Parameterized Constructor"<<endl;
		}
};
main()
{
	Test t,t1(10),t2=10;
}