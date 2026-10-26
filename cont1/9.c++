#include <iostream>
#include <deque>
#include <vector>

using namespace std;

void solve() {
    int n;
    cin >> n;

    deque<int> d;

    
    for (int i = n; i >= 1; i--) {
        d.push_front(i);
        for (int j = 0; j < i; j++) {
            int back_card = d.back();
            d.pop_back();
            d.push_front(back_card);
        }
    }


    for (int i = 0; i < n; i++) {
        cout << d[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}