#include <bits/stdc++.h>
using namespace std;

int main()
{
    int         size = 17;
    vector<int> n    = {17, 13, 12, 7, 8, 9, 14, 15, 1, 2, 6, 4, 5, 16, 3, 10, 11};
    vector<int> ne;
    int         r = 1;

    while(r < size)
    {
        n = ne;
        ne.clear();
        int now = 0, i, j;
        while(now < size)
        {
            i = now;
            j = i + r;
            while(i < now + r && j < now + 2 * r && j < size)
            {
                if(n[i] < n[j])
                {
                    ne.push_back(n[i]);
                    i++;
                }
                else
                {
                    ne.push_back(n[j]);
                    j++;
                }
            }
            while(i < now + r && i < size)
            {
                ne.push_back(n[i]);
                i++;
            }
            while(j < now + 2 * r && j < size)
            {
                ne.push_back(n[j]);
                j++;
            }
            now += r * 2;
        }
        r *= 2;
        for(int k = 0; k < size; k++)
            cout << ne[k] << " ";
        cout << endl;
    }
}
