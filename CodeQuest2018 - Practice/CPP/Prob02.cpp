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
    std::getline(std::cin, text);
    return text;
}

int main() {
    int ncases;
    cin >> ncases;
    input();
    for (int i = 0; i < ncases; i++) {
        const string vowels = "aeiou";
        string text = input();
        int count = 0;
        for (char const &c : text) {
            if (vowels.find(c) != std::string::npos) {
                count++;
            }
        }
        print(count);
    }

    return 0;
}