#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

void heapify(vector<long long>& a, int n, int i){
    int lgs=i;
    int left=2*i+1;
    int right=2*i+2;

    if (left<n && a[left]>a[lgs]){
        lgs=left;
    }
    if (right<n && a[right]>a[lgs]){
        lgs=right;
    }

    if (lgs!=i){
        swap(a[i], a[lgs]);
        heapify(a, n, lgs);
    }
}

void heap_sort(vector<long long>&a){
    int n=a.size();
    for (int i=n/2-1; i>=0; i--){
        heapify(a, n, i);
    }

    for (int i=n-1; i>0; i--){
        swap(a[0], a[i]);
        heapify(a, i, 0);
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin>>n)) return 0;

    vector<long long> a(n);
    for (int i=0; i<n; ++i){
        cin>>a[i];
    }

    heap_sort(a);
    long long min_diff=a[1]-a[0];
    for (int i=1; i<n-1; ++i){
        long long diff=a[i+1]-a[i];
        if (diff<min_diff){
            min_diff=diff;
        }
    }

    bool first=true;
    for (int i=0; i<n-1; ++i){
        if (a[i+1]-a[i]==min_diff){
            if (!first) cout<<" ";
            cout<<a[i]<<" "<<a[i+1];
            first=false;
        }
    }
    cout<<"\n";
    return 0;
}