#include <bits/stdc++.h>
using namespace std;

template<typename T>
class stackk
{
public:
	T st[300000];

	int e = 0;

	int size()
	{
		return e;
	}

	void pop()
	{
		e--;
	}

	void push(const T & i)
	{
		st[++e] = i;
	}

	T top()
	{
		return st[e];
	}
};

int main()
{
	stackk<int> st;

	st.push(1);
	st.push(2);
	st.push(3);


	while(st.size())
	{
		cout << st.top();
		st.pop();
	}
}
