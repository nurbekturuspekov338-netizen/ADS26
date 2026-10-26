#include <iostream>
#include <vector>

using namespace std;

void heapify(vector<long long> heap, int n , int i){
    int lgs=i;
    int left=2*i+1;
    int right=2*i+2;

    if (left<n && heap[left]>heap[lgs]){
        lgs=left;
    } 

    if (right<n && heap[right]>heap[lgs]){
        lgs=right;
    }

    if(lgs!=i){
        swap(heap[i], heap[lgs]);
        heapify(heap, n, lgs);
    }
}

void heap_sort(vector<long long> heap){
    int n=heap.size();
    for(int i=n/2-1; i>=0; i--){
        heapify(heap, n, i);
    }

    for(int i=n-1; i>0; i--){
        swap(heap[0], heap[i]);
        heapify(heap, i, 0);
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if(!(cin>>n>>m)) return 0;

    vector<long long> a(n);
    for (int i=0; i<n; ++i){
        cin>>a[i];
    }
    vector<long long> b(m);
    for (int i=0; i<m; ++i){
        cin>>b[i];
    }

    heap_sort(a);
    heap_sort(b);
    
    int i=0, j=0;
    bool first=true;
    while(i<n && j<m){
        if (a[i]==b[j]){
            if (!first) cout<<" ";
            cout<<a[i];
            first=false;
            i++;
            j++;
        }else if (a[i]<b[j]){
            i++;
        }else{
            j++;
        }
    }
    cout<<'\n';
    return 0;

}
