#include <bits/stdc++.h>
using namespace std;

long long valvec[200001], rvalvec[200001], onevalvec[200001];

inline int lowbit(const int &i)
{
    return i & (-i);
}

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(0);
    int m, n;

    memset(valvec, 0x3f, sizeof(valvec));
    memset(rvalvec, 0x3f, sizeof(rvalvec));

    cin >> m >> n;
    for(long long i = 1 ; i <= m; i++)
    {
        long long j = i;
        long long k;
        cin >> k;
        onevalvec[i] = k;

        while(j < 200001)
        {
            valvec[j] = min(valvec[j], abs(j - i) + k);
            j        += lowbit(j);
        }
        j = 200001 - i;
        while(j < 200001)
        {
            rvalvec[j] = min(rvalvec[j], abs(j - (200001 - i)) + k);
            j         += lowbit(j);
        }
    }

    for(long long i = 0 ; i < n; i++)
    {
        long long cas;
        cin >> cas;
        if(cas == 1)
        {
            long long k, x;
            cin >> k >> x;
            onevalvec[k] = x;
            long long j = k;


            while(j < 200001)
            {
                long long nj = j - 1;
                long long mi = onevalvec[j];
                while(nj > 0 && lowbit(nj) < lowbit(j))
                {
                    mi  = min(mi, abs(j - nj) + valvec[nj]);
                    nj -= lowbit(nj);
                }
                valvec[j] = mi;

                j += lowbit(j);
            }


            j = 200001 - k;


            while(j < 200001)
            {
                long long nj = j - 1;
                long long mi = onevalvec[200001 - j];
                while(nj > 0 && lowbit(nj) < lowbit(j))
                {
                    mi  = min(mi, abs(j - nj) + rvalvec[nj]);
                    nj -= lowbit(nj);
                }
                rvalvec[j] = mi;

                j += lowbit(j);
            }
        }
        else
        {
            long long tar;
            cin >> tar;

            long long j  = tar;
            long long mi = 0x3f3f3f3f3f3f3f3f;
            while(j > 0)
            {
                mi = min(mi, abs(tar - j) + valvec[j]);
                j -= lowbit(j);
            }
            tar = 200001 - tar;
            j   = tar;
            while(j > 0)
            {
                mi = min(mi, abs(tar - j) + rvalvec[j]);
                j -= lowbit(j);
            }

            cout << mi << "\n";
        }
    }
}
