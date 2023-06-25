#include <bits/stdc++.h>
using namespace std;


vector<vector<int> > nodevec(1e5 + 1);
vector<bool>         teamvec(1e5 + 1, 0), boolvec(1e5 + 1, 0);
queue<int>           dealque;
int main()
{
    int m, n;

    cin >> m >> n;


    for(int i = n ; i-- ;)
    {
        int j, k;
        cin >> j >> k;
        j--;
        k--;

        nodevec[j].push_back(k);
        nodevec[k].push_back(j);
    }


    for(int i = 0 ; i < m; i++)
    {
        if(boolvec[i])
            continue;
        boolvec[i] = 1;
        dealque.push(i);
        while(dealque.size())
        {
            int d = dealque.front();
            dealque.pop();
            for(auto&j:nodevec[d])
            {
                if(boolvec[j] == 0)
                {
                    boolvec[j] = 1;
                    teamvec[j] = !teamvec[d];
                    dealque.push(j);
                }
                else if(teamvec[d] == teamvec[j])
                {
                    cout << "IMPOSSIBLE\n";
                    return 0;
                }
            }
        }
    }

    for(int i = 0 ; i < m; i++)
        cout << (teamvec[i]?"1":"2") << " ";
}
