#include<bits/stdc++.h>
using namespace std;

struct Grid
{
    float price;
    int buyornot=-1; //0->buy 1-
};
void getlowmax(float & min,float & max,string type)
{
    ifstream inpu(type);
    min=10000000000.0,max=-1.0;
    float nowprice;
    float nowprices[4];
    float lastprice=-1.0;
    long long int timetemp;
    char a;
    while(inpu>>timetemp)
    {
        inpu>>a>>nowprices[0]>>a>>nowprices[1]>>a>>nowprices[2]>>a>>nowprices[3];
        sort(nowprices,nowprices+4);
        nowprice=(nowprices[1]+nowprices[2])/2.0;

        if(lastprice==-1.0)
        {
            lastprice=nowprice;
            continue;
        }

        if(nowprice>lastprice*1.025||nowprice<lastprice/1.025) continue; // 跳過binance API的BUG數據


        if(nowprice>max)max=nowprice;
        if(nowprice<min)min=nowprice;
        lastprice=nowprice;
    }

}

Caculate(int gridamount,string pricetype)
{
    //string pricetype="btc_bars.csv";
    ifstream inpu(pricetype);

    float minprice,maxprice;
    //getlowmax(minprice,maxprice,pricetype);
    minprice=2300,maxprice=4500;
    Grid grid[gridamount];
    grid[0].price=minprice;
    for(int i=1;i<gridamount;i++)
    {
        grid[i].price=(float)(grid[i-1].price)*pow(maxprice/minprice,(float)1/(gridamount-1));
    }
    //cout<<grid[0].price<<" "<<minprice<<" "<<grid[99].price<<" "<<maxprice<<'\n';

    float nowprice,lastprice;
        float nowprices[4];
    long long int time=-1,timetemp;
    char a;

    float sale=0.0;
    while(inpu>>timetemp)
    {
        inpu>>a>>nowprices[0]>>a>>nowprices[1]>>a>>nowprices[2]>>a>>nowprices[3];
        sort(nowprices,nowprices+4);
        nowprice=(nowprices[1]+nowprices[2])/2.0;
        if(time==-1)
        {
            time=timetemp;
            for(int i=0;i<gridamount;i++)
            {
                if(grid[i].price>nowprice)grid[i].buyornot=1;
                lastprice=nowprice;
            }
            continue;
        } // 處理第一次

        if(nowprice>lastprice*1.025||nowprice<lastprice/1.025) continue; // 跳過binance API的BUG數據

        if(nowprice>lastprice)
        {
            for(int i=0;i<gridamount;i++)
            {
                if(grid[i].price<nowprice&&grid[i].buyornot==1)
                {
                    grid[i].buyornot=0;
                    grid[i-1].buyornot=-1;
                    sale++;
                }
            }
        }

        if(nowprice<lastprice)
        {
            for(int i=gridamount-1;i>=0;i--)
            {
                if(grid[i].price>nowprice&&grid[i].buyornot==-1)
                {
                    grid[i].buyornot=0;
                    grid[i+1].buyornot=1;
                    //sale++;
                }
            }
        }


        lastprice=nowprice;
    }

    //sale/=2; //買賣都算一次所以/=2

    float aprofit=(pow(maxprice/minprice,(float)1/(gridamount-1))-1)*100.0;
    float aprofitinall=(pow(maxprice/minprice,(float)1/(gridamount-1))-1)*100.0/gridamount; //單網格利潤佔總投資額%(可以減掉手續費)
    float timegothrough=(timetemp-time)/1000/60/60/24;
    //cout<<minprice<<" "<<maxprice<<" ";
    cout<<aprofit<<"%,"<<(float)aprofitinall*sale*365.0/timegothrough<<"%\n";//,"<<sale<<"\n";
}

int main()
{
    //ios_base::sync_with_stdio(false);
    //cin.tie(0);
    string type;
    cin>>type;

    type=type+"_bars.csv";

    for(float i=3;i<10000;i*=1.1)Caculate(i,type);

    system("pause");
    return 0;

}