#include<iostream>
using namespace std;
class Test
{
	public:
		int x=12,y=10;
	static int a;
};
int Test :: a=10;
main()
{
	Test t;
	cout<<"before changing on local var"<<endl;
	cout<<t.x<<" and "<<t.y<<endl;
	cout<<"before changing on static var"<<endl;
	cout<<t.a<<endl;
	t.x=100;
	t.y=200;
	t.a=500;
	cout<<"after changing on local var"<<endl;
	cout<<t.x<<" and "<<t.y<<endl;
	cout<<"after changing on static var"<<endl;
	cout<<t.a<<endl;
	Test t1;
	cout<<"after creating new obj no changes on local var when calling from new obj"<<endl;
	cout<<t1.x<<" and "<<t1.y<<endl;
	cout<<"after creating new obj changes on static var its value is same as last value"<<endl;
	cout<<t1.a<<endl;
}