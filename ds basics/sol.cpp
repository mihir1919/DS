#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int t,n,k,i,it,j;
int main()
{
    cin>>t;
    for(it=0;it<t;it++){
        vector<long int> a;
        vector<long int> b;
        cin>>n;
        for(j=0;j<n;j++)
        {
            cin>>k;
            a.push_back(k);
        }
        sort(a.begin(),a.end());
        for(j=0;j<n;j++)
        {
            cin>>k;
            b.push_back(k);
        }
        sort(b.begin(),b.end());
        long sum=0;
        for(i=0;i<n;i++)
        {
            if(a[i]<b[i])
            {
                sum+=a[i];
            }
            else
            {
                sum+=b[i];
            }
        }
        cout<<sum<<endl;

    }
    return 0;
}
