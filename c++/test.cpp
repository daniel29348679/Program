#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

pair<int, int> dp[1 << 20];
ll             num[20];
int main()
{
    cin.tie(0);
    ios::sync_with_stdio(0);
    int m;
    ll  n;
    cin >> m >> n;
    for(int i = 0 ; i < m; i++)
        cin >> num[i];
    dp[0] = {1, 0};
    for(int i = 1 ; i < (1 << m); i++)
    {
        dp[i] = {25, 0};
        for(int j = 0 ; j < m; j++)
            if(i & (1 << j))
            {
                pair<int, int> p = dp[i ^ (1 << j)];
                if(p.second + num[j] <= n)
                    p.second += num[j];
                else
                {
                    p.first++;
                    p.second = num[j];
                }

                dp[i] = min(dp[i], p);
            }
    }
    cout << dp[(1 << m) - 1].first;
}
