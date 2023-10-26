#include <bits/stdc++.h>
using namespace std;


auto lowbit(const & i)
{
    return -i & i;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int n = 10000;
    int node[n + 1];
    int ans[n + 1] = {0};
    int total      = 1;
    for(int i = 1; i < n + 1; i++)
    {
        total  *= 3;
        total  %= 7;
        node[i] = total;
    }

    for(int i = 1; i < n + 1; i++)
        for(int j = i; j < n + 1; j += (-j) & j)
            ans[j] += node[i];
    total = 0;
    for(int i = 1; i < n + 1; i++)
    {
        total += node[i];
        cout << "i= " << i << " node= " << node[i] << " total= " << total << " nodesum= " << ans[i] << " Equivalent eauiroad>>";
        for(int j = i; j > 0; j -= -j & j)
            cout << " " << j;
        cout << '\n';
    }
}
