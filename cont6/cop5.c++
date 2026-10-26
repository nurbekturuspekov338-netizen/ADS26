#include <iostream>
#include <vector>

using namespace std;

void heapify(vector<long long>& a, int n, int i) {
    int smallest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && a[left] < a[smallest]) {
        smallest = left;
    }
    if (right < n && a[right] < a[smallest]) {
        smallest = right;
    }

    if (smallest != i) {
        swap(a[i], a[smallest]);
        heapify(a, n, smallest);
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


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin>>n>>m)) return 0;

    vector<vector<long long> > matrix(n, vector<long long>(m));
    for (int i=0; i<n; ++i){
        for (int j=0; j<m; ++j){
            cin>>matrix[i][j];
        }
    }

    for (int j=0; j<m; ++j){
        vector<long long> col(n);
        for (int i=0; i<n; ++i){
            col[i]=matrix[i][j];
        }
        heap_sort(col);
        for (int i=0; i<n; ++i){
            matrix[i][j]=col[i];
        }
    }

    for (int i=0; i<n; ++i){
        for (int j=0; j<m; ++j){
            cout<<matrix[i][j]<<(j==m-1 ? "" : " ");
        }
        cout<<'\n';
    }
    return 0;
}