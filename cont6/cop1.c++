#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool is_vowel(char c){
    char lower_c=tolower(c);
    return 'a'==c || 'e'==c || 'i'==c || 'o'==c ||'u'==c;
}

bool greater_c(char a, char b){
    bool v1=is_vowel(a);
    bool v2= is_vowel(b);
    if (v1!=v2){
        return !v1;
    }else{
        return a>b;
    }
}

void heapify(string& s, int n, int i){
    int lgs=i;
    int left=2*i+1;
    int right=2*i+2;
    if (left<n && greater_c(s[left], s[lgs])){
        lgs=left;
    }
    if (right<n && greater_c(s[lgs], s[right])){
        lgs=right;
    }

    if (lgs!=i){
        swap(s[i], s[lgs]);
        heapify(s, n, lgs);
    }
}

void heap_sort(string& s, int n){
    for (int i=n/2-1; i>=0; i--){
        heapify(s, n, i);
    }

    for (int i=n-1; i>0; i--){
        swap(s[0], s[i]);
        heapify(s, i, 0);
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if(cin>>n){
        string s;
        cin>>s;
        heap_sort(s, n);
        cout<<s<<'\n';
    }
    return 0;
}