#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    if (n < 3) {
        cout << 0 << "\n";
        return 0;
    }

    int max_idx = (n - 1) & ~1;
    vector<int> p(max_idx, 0);
    int j = 0;
    int ans = 0;

    for (int i = 1; i < max_idx; ++i) {
        while (j > 0 && s[i] != s[j]) {
            j = p[j - 1];
        }
        if (s[i] == s[j]) {
            j++;
            p[i] = j;
        }
        if (i & 1) {
            int k = (i + 1) >> 1;
            if (j >= k && k % (i + 1 - j) == 0) {
                ans++;
            }
        }
    }

    cout << ans << "\n";
    return 0;
}