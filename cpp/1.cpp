// g++ 1.cpp --std=c++1z; ./a.out

#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <unordered_map>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int Part1(const vector<int>& left_list, const vector<int>& right_list) {
    int result = 0;
    for (int i = 0; i < left_list.size(); ++i) {
        result += abs(left_list[i] - right_list[i]);
    }
    return result;
}

int Part2(const vector<int>& left_list, const vector<int>& right_list) {
    unordered_map<int, int> right_counter;
    for (int i = 0; i < right_list.size(); ++i) {
        const int number = right_list[i];
        auto itr = right_counter.find(number);
        if (itr == right_counter.end()) {
            right_counter.emplace(number, 1);
        } else {
            itr->second += 1;
        }
    }

    int result = 0;
    for (int i = 0; i < left_list.size(); ++i) {
        const int number = left_list[i];
        auto itr = right_counter.find(number);
        if (itr == right_counter.end()) {
            continue;
        }
        result += itr->second * number;
    }
    return result;
}

int main() {
    ifstream file("1.txt");
    if (!file.is_open()) {
        cerr << "Couldn't open file" << endl;
        return 1;
    }

    vector<int> left_list;
    vector<int> right_list;

    string line;
    while (getline(file, line)) {
        istringstream ss(line);
        int left, right;
        ss >> left;
        ss >> right;
        left_list.push_back(left);
        right_list.push_back(right);
    }

    sort(left_list.begin(), left_list.end());
    sort(right_list.begin(), right_list.end());

    cout << Part1(left_list, right_list) << endl;
    cout << Part2(left_list, right_list) << endl;

    file.close();
    return 0;
}
