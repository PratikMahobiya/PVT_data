#include<iostream>
using namespace std;
class Test
{
	private:
		int a,b;
	private:
		Test()
		{
			cout<<"0- args = Default Constructor"<<endl;
		}
		Test(int a)
		{
			cout<<"1- args = Parameterized Constructor As Copy Constructor"<<endl;
		}
		Test(Test &t3)
		{
			cout<<"3- args = Copy Constructor"<<endl;
			for (int i=0;i<=5;i++)
			{
				cout<<"value of i is "<<i<<endl;
			}
		}
		
};
main()
{
	Test t,t1(10);
	Test t2(t1);
}