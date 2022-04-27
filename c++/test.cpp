#include<bits/stdc++.h>
using namespace std;



int main()
{
    //ifstream cinn("test_input.txt");
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    //int ti=clock();

    int t;
    int n,x,a,b,aa,bb;
    cin>>n>>x;
    int cits[n+1]={-1};

    for(int k=0;k<x;k++)
    {
        //for(int kk=1;kk<=n;kk++) cout<<kk<<" "<<cits[kk]<<"\n";
        cin>>a>>b;
        aa=a;bb=b;
        while(cits[a]!=0) a=cits[a];
        while(cits[b]!=0) b=cits[b];
        if(a!=b)
        {
            if(aa==a)
            {
                cits[a]=b;

            }
            else if(bb==b)
            {
               cits[b]=a;

            }
            else
            {
                cits[a]=b;
                while(cits[aa]!=b)
                {
                    t=aa;
                    aa=cits[aa];
                    cits[t]=b;
                }
            }
        }

    }
    int total=-1;
    for(int k=1;k<=n;k++)
    {
        if(cits[k]==0)
        {
            total++;
        }
    }
    cout<<total<<"\n";

    int last=-1;
    for(int k=1;k<=n;k++)
    {
        if(cits[k]==0)
        {
            if(last==-1)
            {
                last=k;
            }
            else
            {
                cout<<last<<" "<<k<<"\n";
                last=k;
            }
        }
    }

    //cout<<"COST   "<<(float)(clock()-ti)/1000<<"s";
}