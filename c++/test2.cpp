#include <bits/stdc++.h>
#define int    long long
#define fi     first
#define se     second
#define pii    pair<int, int>
#define all(x)    x.begin(), x.end()

using namespace std;
typedef long long ll;

struct flight
{
    int time;
    int fee;
    int to;
};

struct node
{
    int            total;
    int            fat;
    vector<flight> childvec;
};

vector<node>     nodevec;
vector<flight>   flivec;
map<string, int> namemap;
vector<string>   strvec;
set<string>      nameset;

signed main()
{
    //ios::sync_with_stdio(0);
    //cin.tie(0);

    string str;

    while(cin >> str)
    {
        if(str[str.size() - 1] == ' ')
            str = str.substr(0, str.size() - 1);
        strvec.push_back(str);
    }

    int siz = strvec.size() / 4;

    for(int i = 0 ; i < strvec.size() / 2; i++)
        nameset.insert(strvec[i]);
    int            ii = 0;
    vector<string> names;

    for(auto i = nameset.begin() ; i != nameset.end(); i++)
    {
        nodevec.push_back({9999999, -1, {}});
        namemap[*i] = ii++;
        names.push_back(*i);
    }


    for(int i = 0 ; i < strvec.size() / 4; i++)
        nodevec[namemap[strvec[i]]].childvec.push_back({stoi(strvec[i + siz * 2]), stoi(strvec[i + siz * 3]), namemap[strvec[i + siz]]});
    queue<int> qu;

    qu.push(namemap["SEA"]);
    nodevec[namemap["SEA"]].total = 0;
    while(qu.size())
    {
        int now = qu.front();
        qu.pop();


        for(int i = 0 ; i < nodevec[now].childvec.size(); i++)
        {
            flight fl = nodevec[now].childvec[i];
            if(nodevec[now].total + fl.time * 3 + fl.fee < nodevec[fl.to].total)
            {
                nodevec[fl.to].total = nodevec[now].total + fl.time * 3 + fl.fee;
                nodevec[fl.to].fat   = now;
                qu.push(fl.to);
            }
        }
    }

    //for(int i = 0 ; i < nodevec.size(); i++)
    //cout << nodevec[i].total << " " << nodevec[i].fat << " " << nodevec[i].childvec.size() << endl;

    vector<string> trip;
    int            i = namemap["ORD"];

    while(i != -1)
    {
        trip.push_back(names[i]);
        i = nodevec[i].fat;
    }

    for(int i = trip.size() - 1 ; i >= 1; i--)
        cout << trip[i] << "-" << trip[i - 1] << " ";
}
