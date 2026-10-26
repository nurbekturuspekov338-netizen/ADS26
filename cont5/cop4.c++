#include <iostream>
#include <vector>

using namespace std;

void sift_down(vector<long long>& heap, int i){
    int size=heap.size();
    while (true){
        int largest=i;
        int left=2*i+1;
        int right=2*i+2;

        if (left<size && heap[left]>heap[largest]){
            largest=left;
        }
        if (right<size && heap[right]>heap[largest]){
            largest=right;
        }
        if (largest!=i){
            swap(heap[i], heap[largest]);
            i=largest;
        }else{
            break;
        }
    }
}

void sift_up(vector<long long>& heap, int i){
    while (i>0){
        int parent=(i-1)/2;
        if (heap[i]>heap[parent]){
            swap(heap[i], heap[parent]);
            i=parent;
        }else{
            break;
        }
    }
}

long long heappop(vector<long long>& heap){
    long long root=heap[0];
    long long last = heap.back();
    heap.pop_back();
    if (!heap.empty()){
        heap[0]=last;
        sift_down(heap, 0);
    }
    return root;
}

void heappush(vector<long long>&heap, long long val){
    heap.push_back(val);
    sift_up(heap, heap.size() - 1);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    if (!(cin>>n>>m)) return 0;

    vector<long long> heap;
    for (int i=0; i<n; ++i){
        cin>>heap[i];
    }

    for (int i=(n-2)/2; i>=0; --i){
        sift_down(heap, i);
    }

    int operations=0;

    while (!(heap.empty()) && heap[0]<m){
        if (heap.size()<2){
            cout<<-1<<"\n";
            return 0;
        }

        long long d_least=heappop(heap);
        long long d_second=heappop(heap);

        long long new_d=d_least+2*d_second;
        heappush(heap, new_d);

        operations++;
    }
    cout<<operations<<'\n';
    return 0;

}