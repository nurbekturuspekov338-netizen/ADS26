#include <iostream>
#include <queue>

using namespace std;

bool beats(int a, int b) {
    if (a == 0 && b == 9) return true;  
    if (a == 9 && b == 0) return false; 
    return a > b;                      
}

int main() {
    queue<int> b;
    queue<int> n;

    for (int i = 0; i < 5; i++) {
        int card;
        cin >> card;
        b.push(card);
    }
    for (int i = 0; i < 5; i++) {
        int card;
        cin >> card;
        n.push(card);
    }

    int moves = 0;
    const int LIMIT = 1000000;

    
    while (!b.empty() && !n.empty() && moves < LIMIT) {
        moves++;
        int b_card = b.front(); b.pop();
        int n_card = n.front(); n.pop();

        if (beats(b_card, n_card)) {
            b.push(b_card);
            b.push(n_card);
        } else {
            n.push(b_card);
            n.push(n_card);
        }
    }

    if (b.empty()) {
        cout << "Nursik " << moves << "\n";
    } else if (n.empty()) {
        cout << "Boris " << moves << "\n";
    } else {
        cout << "blunder\n";
    }

    return 0;
}