#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    const int MAX_VALUE = 100000;
    vector<int> count(MAX_VALUE + 1, 0);

    for (int i = 0; i < N; ++i) {
        int num;
        cin >> num;
        ++count[num];
    }

    for (int i = 0; i <= MAX_VALUE; ++i) {
        while (count[i]--) {
            cout << i << ' ';
        }
    }

    cout << '\n';
    return 0;
}
