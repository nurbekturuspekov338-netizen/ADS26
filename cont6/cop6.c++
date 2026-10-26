#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

using namespace std;

struct Student{
    string lastname;
    string firstname;
    double gpa;
};

double mark_to_gpa(const string& mark){
    if (mark=="A+") return 4.00;
    if (mark=="A") return 3.75;
    if (mark=="B+") return 3.50;
    if (mark=="B") return 3.00;
    if (mark=="C+") return 2.50;
    if (mark=="C") return 2.00;
    if (mark=="D+") return 1.50;
    if (mark=="D") return 1.00;
    return 0.0;
}

bool compare_students(const Student& a, const Student& b){
    if (a.gpa!=b.gpa) return a.gpa<b.gpa;
    if (a.lastname!=b.lastname) return a.lastname<b.lastname;
    return a.firstname<b.firstname;
}

void heapify(vector<Student>& a, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && compare_students(a[largest], a[left])) {
        largest = left;
    }
    if (right < n && compare_students(a[largest], a[right])) {
        largest = right;
    }

    if (largest != i) {
        swap(a[i], a[largest]);
        heapify(a, n, largest);
    }
}

void heap_sort(vector<Student>& a) {
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

    int n;
    if(!(cin>>n)) return 0;

    vector<Student> students(n);
    for (int i=0; i<n; ++i){
        cin>>students[i].lastname>>students[i].firstname;
        int m;
        cin>>m;
        double total_gpa_credits=0.0;
        int total_credits=0;
        for (int j=0; j<m; ++j){
            string mark;
            int credits;
            cin>>mark>>credits;
            total_gpa_credits+=mark_to_gpa(mark)*credits;
            total_credits+=credits;
        students[i].gpa = (total_credits > 0) ? (total_gpa_credits / total_credits) : 0.0;
    }

    heap_sort(students);

    cout << fixed << setprecision(3);
    for (int i = 0; i < n; ++i) {
        cout << students[i].lastname << " " << students[i].firstname << " " << students[i].gpa << "\n";
    }

    return 0;

    }
}