#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> li_n(n);
    unordered_set<int> s;

    for (int i = 0; i < n; ++i) {
        cin >> li_n[i];
        s.insert(li_n[i]); // 검색 속도를 위해 set에 저장
    }

    int m;
    cin >> m;
    vector<int> li_m(m);

    for (int i = 0; i < m; ++i) {
        cin >> li_m[i];
    }

    for (int i = 0; i < m; ++i) {
        if (s.count(li_m[i])) {
            cout << 1 << " ";
        } else {
            cout << 0 << " ";
        }
    }

    cout << endl;
    return 0;
}
