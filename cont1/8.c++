#include <iostream>
#include <stack>

using namespace std;

int main() {
    int n;
    cin >> n;

    stack<int> st;

    for (int i = 0; i < n; i++) {
        int age;
        cin >> age;
        while (!st.empty() && st.top() >= age) {
            st.pop();
        }

        if (st.empty()) {
            cout << -1 << " ";
        } else {
            cout << st.top() << " ";
        }

        st.push(age);
    }

    return 0;
}
