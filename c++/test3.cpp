#include <bits/stdc++.h>
#define int	   long long
#define fi	   first
#define se	   second
#define pii	   pair<int, int>
#define all(x)    x.begin(), x.end()
#define it	   map<char, int>::iterator

using namespace std;
typedef long long ll;


signed main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	int	   n;
	string s;
	cin >> n;
	set<int> v[n];
	getline(cin, s);
	for(int i = 0; i < n; ++i)
	{
		getline(cin, s);
		s.push_back(',');
		int res = 0;
		for(int j = 0 ; j < (int)s.length(); ++j)
		{
			if(s[j] == ',')
			{
				v[i].insert(res);
				//cout << res << endl;
				res = 0;
			}
			else
			{
				res *= 10;
				res += s[j] - '0';
			}
		}
	}

	map<int, int> m;
	for(int i = 0; i < n; ++i)
		for(auto k = v[i].begin(); k != v[i].end(); ++k)
			m[*k]++;

	int ans = INT_MAX;
	for(int ii = 0 ; ii < n; ii++)
	{
		int tem = 99999;
		for(int j:v[ii])
			tem = min(tem, m[j]);
		ans = min(ans, tem);
	}
	cout << ans;
}
