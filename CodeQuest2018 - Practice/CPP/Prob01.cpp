//
// Created by Henry on 6/14/2019.
//

#include <iostream>
using namespace std;

void print(string* text) {
    cout << text << "\n";
}
void print(int num) {
    cout << num << "\n";
}


int main() {
    int ncases;
    cin >> ncases;
    for (int i = 0; i < ncases; i++) {
        int cnum;
        cin >> cnum;
        if (cnum >= 70) {
            cout << "PASS\n";
        } else {
            cout << "FAIL\n";
        }
    }

    return 0;
}