#include <iostream>
#include <vector>
#include <string>

using namespace std;

Struct User{
    string original;
    string current;
};

int partition(vector<User>& a, int low, int high){
    string pivot=a[high].original;
    int i=low-1;

    for (int j=low, j<high; j++){
        if (a[j].original<pivot){
            i++;
            swap(a[i], a[j]);
        }
    }
    swap(a[i+1], a[high]);
    return i+1;
}

void quick_sort(vector<User>& a, int low, int high){
    if (low<high){
        int pi=partition(a, low, high);
        quick_sort(a, low, pi-1);
        quick_sort(a, pi+1, high);
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<User> users;
    for (int i=0; i<n; ++i){
        string old_nick, new_nick;
        cin>>old_nick>>new_nick;

        bool found=false;
        for(size_t j=0; j<users.size(); ++j){
            if (users[j].current==old_nick){
                users[j].current=new_nick;
                found=true;
                break;
            }
        }

    if (!found) {
            User u;
            u.original = old_nick;
            u.current = new_nick;
            users.push_back(u);
        }
    }

    if (!users.empty()) {
        quick_sort(users, 0, users.size() - 1);
    }

    cout << users.size() << "\n";
    for (size_t i = 0; i < users.size(); ++i) {
        cout << users[i].original << " " << users[i].current << "\n";
    }

    return 0;
}  