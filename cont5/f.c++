#include <iostream>
#include <vector>
#include <string>

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

    int q;
    size_t k;
    if (!(cin >> q >> k)) return 0;

    vector<long long> heap;
    long long current_sum = 0;

    for (int i = 0; i < q; ++i) {
        string type;
        if (!(cin >> type)) break; 

        if (type == "insert") {
            long long val;
            cin >> val;

            if (heap.size() < k) {
                heappush(heap, val);
                current_sum += val;
            } else if (k > 0 && val > heap[0]) {
                current_sum -= heappop(heap);
                heappush(heap, val);
                current_sum += val;
            }
        } else if (type == "print") {
            cout << current_sum << "\n";
        }
    }

    return 0;
}