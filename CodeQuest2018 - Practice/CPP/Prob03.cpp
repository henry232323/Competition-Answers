//
// Created by Henry on 6/14/2019.
//

#include <iostream>
using namespace std;

void print(string text) {
    cout << text << "\n";
}
void print(int num) {
    cout << num << "\n";
}

string input()
{
    string text;
    getline(std::cin, text);
    return text;
}

int main() {
    int ncases;
    cin >> ncases;
    input();
    for (int i = 0; i < ncases; i++) {
        int n;
        cin >> n;
        input();
        if (n % 10 == 1 and n / 10 != 1) {
            cout << n << "st\n";
        } else if (n % 10 == 2 and n / 10 != 1) {
            cout << n << "nd\n";
        } else if (n % 10 == 3) {
            cout << n << "rd\n";
        } else {
            cout << n << "th\n";
        }
    }

    return 0;
}