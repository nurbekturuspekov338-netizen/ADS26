#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

using namespace std;

struct Date{
    int day;
    int month;
    int year;
};

bool compare_dates(const Date& a, const Date& b){
    if (a.year!=b.year) return a.year<b.year;
    if (a.month!=b.month) return a.month<b.month;
    return a.day<b.day;
}

void heapify(vector<Date>& a, int n, int i){
    int lgs=i; 
    int left=2*i+1;
    int right=2*i+2;
    
    if (left<n && compare_dates(a[lgs], a[left])){
        lgs=left;
    }
    if (right<n && compare_dates(a[lgs], a[right])){
        lgs=right;
    }
    if (lgs!=i){
        swap(a[i], a[lgs]);
        heapify(a, n, lgs);
    }
}

void heap_sort(vector<Date>& a){
    int n=a.size();
    for (int i=n/2-1; i>=0; i--){
        heapify(a, n, i);
    }
    for (int i=n-1; i>0; i--){
        swap(a[0], a[i]);
        heapify(a, i, 0);
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin>>n)) return 0;

    vector<Date> dates(n);
    for (int i=0; i<n; ++i){
        string s;
        cin>>s;
        dates[i].day=(s[0]-'0')*10+(s[1]-'0');
        dates[i].month=(s[3]-'0')*10+(s[4]-'0');
        dates[i].year=(s[6]-'0')*1000+(s[7]-'0')*100+(s[8]-'0')*10+(s[9]-'0');
    }

    heap_sort(dates);
    for (int i=0; i<n; ++i){
        cout<<setfill('0')<<setw(2)<<dates[i].day<<"-"
        << setfill('0')<<setw(2)<<dates[i].month<<'-'
        <<setfill('0')<<setw(4)<<dates[i].year<<'\n';
    }
    return 0;
}