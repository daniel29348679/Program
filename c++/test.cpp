#include <bits/stdc++.h>
using namespace std;
typedef long long ll;


int main()
{
    int i;

    cin >> i;
    for(int j = 3 ; j < i; j++)
    {
        for(int k = 1 ; k < j ; k++)
            cout << string(j, ' ') << endl;
        cout << "•" << string(j - 2, '_') << "•" << endl;
    }
}
