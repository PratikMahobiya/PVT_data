#include<iostream>
using namespace std;
class Test
{
	private:
		int a,b;
	public:
		Test()
		{
			cout<<"AA GYA BHAIYA CONSTRUCTOR"<<endl;
		}
		~Test()
		{
			cout<<"AA GYA BHAIYA DESTRUCTOR"<<endl;
		}
};
main()
{
	Test t;
	
}