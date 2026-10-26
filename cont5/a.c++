#include <iostream>
#include <vector>

using namespace std;

void sift_down(vector<long long>& heap, int i) {
    int size = heap.size();
    while (true) {
        int smallest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < size && heap[left] < heap[smallest]) {
            smallest = left;
        }
        if (right < size && heap[right] < heap[smallest]) {
            smallest = right;
        }

        if (smallest != i) {
            swap(heap[i], heap[smallest]);
            i = smallest;
        } else {
            break;
        }
    }
}

void sift_up(vector<long long>& heap, int i) {
    while (i > 0) {
        int parent = (i - 1) / 2;
        if (heap[i] < heap[parent]) {
            swap(heap[i], heap[parent]);
            i = parent;
        } else {
            break;
        }
    }
}

long long heappop(vector<long long>& heap) {
    long long root = heap[0];
    long long last = heap.back();
    heap.pop_back();
    if (!heap.empty()) {
        heap[0] = last;
        sift_down(heap, 0);
    }
    return root;
}

void heappush(vector<long long>& heap, long long val) {
    heap.push_back(val);
    sift_up(heap, heap.size() - 1);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n) || n <= 1) {
        cout << 0 << "\n";
        return 0;
    }

    vector<long long> heap(n);
    for (int i = 0; i < n; ++i) {
        cin >> heap[i];
    }

    for (int i = (n - 2) / 2; i >= 0; --i) {
        sift_down(heap, i);
    }

    long long total_cost = 0;

    while (heap.size() > 1) {
        long long first = heappop(heap);
        long long second = heappop(heap);

        long long cost = first + second;
        total_cost += cost;

        heappush(heap, cost);
    }

    cout << total_cost << "\n";

    return 0;
}