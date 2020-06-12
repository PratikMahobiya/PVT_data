#include<iostream>
using namespace std;
class Test
{
	public:
		int x=20,y=10;
	void add(int x,int y)
	{
		cout<<"Addition of "<<x<<" and "<<y<<"= "<<x+y<<endl;
		cout<<"Addition of "<<this->x<<" and "<<this->y<<"= "<<this->x+this->y;
		
	}
};
main()
{
	Test t;
	t.add(100,200);
}