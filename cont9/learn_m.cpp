#include <iostream>
#include <string>
#include <vector>
#include <cassert>
#include <random>

using namespace std;

namespace Algorithms {

    // 1. PREFIX FUNCTION  pi[i] = length of the longest proper border of s[0..i]
    //    O(m) time (amortized argument: k grows by at most 1 per step)
    vector<int> prefixFunction(const string& s) {
        int m = static_cast<int>(s.size());
        vector<int> pi(m, 0);
        for (int i = 1; i < m; ++i) {
            int k = pi[i - 1];              // longest border of s[0..i-1]
            while (k > 0 && s[i] != s[k]) {
                k = pi[k - 1];              // fall back to the next shorter border
            }
            if (s[i] == s[k]) {
                k++;                        // extend the border by one character
            }
            pi[i] = k;
        }
        return pi;
    }

    // 2. KMP SEARCH  returns every start index of pattern in text (overlaps included)
    //    O(n + m) time, O(m) extra memory
    vector<int> kmpSearch(const string& text, const string& pattern) {
        int n = static_cast<int>(text.size());
        int m = static_cast<int>(pattern.size());
        vector<int> result;
        if (m == 0) {
            // Convention: the empty pattern occurs at every position 0..n
            for (int i = 0; i <= n; ++i) {
                result.push_back(i);
            }
            return result;
        }
        if (m > n) {
            return result;
        }

        vector<int> pi = prefixFunction(pattern);
        int q = 0;                          // number of pattern characters matched
        for (int i = 0; i < n; ++i) {
            while (q > 0 && text[i] != pattern[q]) {
                q = pi[q - 1];              // shift the pattern, keep the border
            }
            if (text[i] == pattern[q]) {
                q++;
            }
            if (q == m) {
                result.push_back(i - m + 1);
                q = pi[m - 1];              // continue: allows overlapping matches
            }
        }   
        return result;
    }

    // 3. NAIVE MATCHING  O(n * m) worst case, used as the reference answer
    vector<int> naiveSearch(const string& text, const string& pattern) {
        int n = static_cast<int>(text.size());
        int m = static_cast<int>(pattern.size());
        vector<int> result;
        for (int s = 0; s + m <= n; ++s) {
            int j = 0;
            while (j < m && text[s + j] == pattern[j]) {
                j++;
            }
            if (j == m) {
                result.push_back(s);
            }
        }
        return result;
    }

    // Brute-force prefix function: try every border length from longest to shortest
    vector<int> prefixFunctionBrute(const string& s) {
        int m = static_cast<int>(s.size());
        vector<int> pi(m, 0);
        for (int i = 0; i < m; ++i) {
            for (int len = i; len >= 1; --len) {
                if (s.compare(0, len, s, i - len + 1, len) == 0) {
                    pi[i] = len;
                    break;
                }
            }
        }
        return pi;
    }

    // 4. APPLICATIONS
    int countOccurrences(const string& text, const string& pattern) {
        return static_cast<int>(kmpSearch(text, pattern).size());
    }

    // Smallest p > 0 with s[i] == s[i + p] for all valid i  (p = n - pi[n-1])
    int shortestPeriod(const string& s) {
        int n = static_cast<int>(s.size());
        if (n == 0) {
            return 0;
        }
        vector<int> pi = prefixFunction(s);
        return n - pi[n - 1];
    }

    // Length of the shortest t with s = t + t + ... + t  (n itself if no such t)
    int compressedLength(const string& s) {
        int n = static_cast<int>(s.size());
        int p = shortestPeriod(s);
        if (n > 0 && n % p == 0) {
            return p;
        }
        return n;
    }

} // namespace Algorithms

int main() {
    cout << "========================================================\n";
    cout << " KBTU ADS-2026: Week 10 - Knuth-Morris-Pratt (C++)\n";
    cout << "========================================================\n\n";

    // 1. Prefix function on the lecture examples
    assert(Algorithms::prefixFunction("ABABCABAB") == vector<int>({0, 0, 1, 2, 0, 1, 2, 3, 4}));
    assert(Algorithms::prefixFunction("AABAAAB") == vector<int>({0, 1, 0, 1, 2, 2, 3}));
    assert(Algorithms::prefixFunction("").empty());
    assert(Algorithms::prefixFunction("Z") == vector<int>({0}));
    cout << "[Test Passed] Prefix function matches the hand-computed tables.\n";

    // 2. Search on the lecture example (two overlapping occurrences)
    string text = "ABABABCABABCABAB";
    assert(Algorithms::kmpSearch(text, "ABABCABAB") == vector<int>({2, 7}));
    cout << "[Test Passed] KMP finds the overlapping matches at 2 and 7.\n";

    // 3. Edge cases
    assert(Algorithms::kmpSearch("aaaaa", "aaa") == vector<int>({0, 1, 2}));
    assert(Algorithms::kmpSearch("abc", "") == vector<int>({0, 1, 2, 3}));
    assert(Algorithms::kmpSearch("", "") == vector<int>({0}));
    assert(Algorithms::kmpSearch("", "a").empty());
    assert(Algorithms::kmpSearch("ab", "abc").empty());
    assert(Algorithms::kmpSearch("abc", "abc") == vector<int>({0}));
    assert(Algorithms::kmpSearch("abc", "abd").empty());
    assert(Algorithms::naiveSearch("abc", "") == vector<int>({0, 1, 2, 3}));
    cout << "[Test Passed] Edge cases: overlaps, empty pattern/text, pattern longer than text.\n";

    // 4. Randomized comparison against brute force (small alphabet => many overlaps)
    mt19937 rng(2026);
    for (int iter = 0; iter < 3000; ++iter) {
        int alpha = 1 + static_cast<int>(rng() % 3);
        int n = static_cast<int>(rng() % 30);
        int m = static_cast<int>(rng() % 6);
        string t;
        string p;
        for (int i = 0; i < n; ++i) {
            t += static_cast<char>('a' + rng() % alpha);
        }
        for (int i = 0; i < m; ++i) {
            p += static_cast<char>('a' + rng() % alpha);
        }
        vector<int> expected = Algorithms::naiveSearch(t, p);
        assert(Algorithms::kmpSearch(t, p) == expected);
        assert(Algorithms::prefixFunction(t) == Algorithms::prefixFunctionBrute(t));
    }
    cout << "[Test Passed] 3000 random cases agree with brute force.\n";

    // 5. Applications on concrete strings
    assert(Algorithms::countOccurrences("abababab", "abab") == 3);
    assert(Algorithms::shortestPeriod("abcabcab") == 3);
    assert(Algorithms::compressedLength("abcabcab") == 8);
    assert(Algorithms::compressedLength("abcabcabc") == 3);
    assert(Algorithms::shortestPeriod("AABAAAB") == 4);
    cout << "[Test Passed] Occurrence count, shortest period and compression.\n";
    cout << "========================================================\n";
    return 0;
}