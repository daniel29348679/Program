#include <bits/stdc++.h>
#define int	   long long
#define fi	   first
#define se	   second
#define pii	   pair<int, int>
#define all(x)    x.begin(), x.end()

using namespace std;
typedef long long ll;

struct flight
{
	string n1;
	string n2;
	int	   time;
	int	   fee;
}


int getint()
{
	char c;

	if(en)
		return -999998;

	cin >> c;
	if(c == ']')
		return -999998;

	if(c == '[')
		cin >> c;


	if(c == 'n')
	{
		cin >> c >> c >> c >> c;
		return -999999;
	}

	int total = c - '0';

	while(cin >> c && (c <= '9' && '0' <= c))
	{
		total *= 10;
		total += c - '0';
	}
	if(c == ']')
		en = 1;
	return total;
}

signed main()
{
	//ios::sync_with_stdio(0);
	//cin.tie(0);

	childvec.push_back({});
	numvec.push_back(0);
	int index = 0;
	int now;   //= getint();
	while(now = getint(), now != -999998)
	{
		if(now == -999999)
		{
			index++;
			continue;
		}
		childvec.push_back({});
		childvec[index].push_back(numvec.size());
		numvec.push_back(now);
	}

	dfs(0);


	//now = getint();


	cout << ma;
}
