#include <iostream>
#include <vector>

using namespace std;

void sift_down(vector<long long>& heap, int i){
    int size = heap.size();
    while (true){
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        if (left < size && heap[left] > heap[largest]){
            largest = left;
        }
        if (right < size && heap[right] > heap[largest]){
            largest = right;
        }

        if (largest != i){
            swap(heap[i], heap[largest]);
            i = largest;
        } else {
            break;
        }
    }
}

void sift_up(vector<long long>& heap, int i){
    while (i > 0){
        int parent = (i - 1) / 2;
        if (heap[i] > heap[parent]){
            swap(heap[i], heap[parent]);
            i = parent;
        } else {
            break;
        }
    }
}

long long heappop(vector<long long>& heap){
    long long root = heap[0];
    long long last = heap.back();
    heap.pop_back();
    if (!heap.empty()){
        heap[0] = last;
        sift_down(heap, 0);
    }
    return root;
}

// Добавлена ссылка (&)
void heappush(vector<long long>& heap, long long val){
    heap.push_back(val);
    sift_up(heap, heap.size() - 1);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n) || n < 1){
        cout << 0 << "\n";
        return 0;
    }

    vector<long long> heap(n);
    for (int i = 0; i < n; ++i){
        cin >> heap[i];
    }

    for (int i = (n - 2) / 2; i >= 0; --i){
        sift_down(heap, i);
    }

    while (heap.size() > 1){
        long long y = heappop(heap);
        long long x = heappop(heap);

        if (y != x){
            heappush(heap, y - x);
        }
    }

    if (heap.empty()){
        cout << 0 << '\n';
    } else {
        cout << heap[0] << '\n';
    }

    return 0;
}