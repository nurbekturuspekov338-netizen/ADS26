#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;

int partition(vector<char>& a, int low, int high) {
    int random_idx = low + rand() % (high - low + 1);
    swap(a[random_idx], a[high]);

    char pivot = a[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (a[j] < pivot) {
            i++;
            swap(a[i], a[j]);
        }
    }
    swap(a[i + 1], a[high]);
    return i + 1;
}

void quick_sort(vector<char>& a, int low, int high) {
    if (low < high) {
        int pi = partition(a, low, high);
        quick_sort(a, low, pi - 1);
        quick_sort(a, pi + 1, high);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<char> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    char k;
    cin >> k;

    if (n > 0) quick_sort(a, 0, n - 1);

    char ans = a[0];
    for (int i = 0; i < n; ++i) {
        if (a[i] > k) {
            ans = a[i];
            break;
        }
    }

    cout << ans << "\n";

    return 0;
}