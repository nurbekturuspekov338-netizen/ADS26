#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool is_vowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

bool compare_chars(char a, char b) {
    bool v1 = is_vowel(a);
    bool v2 = is_vowel(b);
    if (v1 != v2) {
        return v1;
    }
    return a < b;
}

void heapify(string& s, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && compare_chars(s[largest], s[left])) {
        largest = left;
    }

    if (right < n && compare_chars(s[largest], s[right])) {
        largest = right;
    }

    if (largest != i) {
        swap(s[i], s[largest]);
        heapify(s, n, largest);
    }
}

void heap_sort(string& s, int n) {
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(s, n, i);
    }

    for (int i = n - 1; i > 0; i--) {
        swap(s[0], s[i]);
        heapify(s, i, 0);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (cin >> n) {
        string s;
        cin >> s;
        heap_sort(s, n);
        cout << s << "\n";
    }
    return 0;
}