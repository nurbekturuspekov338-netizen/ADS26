#include <iostream>
#include <vector>

using namespace std;

void heapify(vector<long long>& a, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && a[left] > a[largest]) {
        largest = left;
    }
    if (right < n && a[right] > a[largest]) {
        largest = right;
    }

    if (largest != i) {
        swap(a[i], a[largest]);
        heapify(a, n, largest);
    }
}

void heap_sort(vector<long long>& a) {
    int n = a.size();
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(a, n, i);
    }
    for (int i = n - 1; i > 0; i--) {
        swap(a[0], a[i]);
        heapify(a, i, 0);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<long long> b(m);
    for (int i = 0; i < m; ++i) {
        cin >> b[i];
    }

    heap_sort(a);
    heap_sort(b);

    int i = 0, j = 0;
    bool first = true;
    while (i < n && j < m) {
        if (a[i] == b[j]) {
            if (!first) cout << " ";
            cout << a[i];
            first = false;
            i++;
            j++;
        } else if (a[i] < b[j]) {
            i++;
        } else {
            j++;
        }
    }
    cout << "\n";

    return 0;
}