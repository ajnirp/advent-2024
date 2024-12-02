// g++ 2.cpp 2.hpp; ./a.out

#include <cmath>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

#include "2.hpp"

using namespace std;

namespace advent2024 {

const vector<int> CopyWithIndexSkip(const vector<int>& arr, const int i) {
    vector<int> result;
    result.reserve(arr.size()-1);
    for (int j = 0; j < arr.size(); ++j) {
        if (i == j) { continue; }
        result.push_back(arr[j]);
    }
    return result;
}

bool TryWithTwoCandidates(const vector<int>& arr, const int i, const int skips_remaining) {
    if (skips_remaining < 0) { return false; }
    const auto candidate1 = CopyWithIndexSkip(arr, i);
    const auto candidate2 = CopyWithIndexSkip(arr, i+1);
    return IsSafe(candidate1, skips_remaining) or IsSafe(candidate2, skips_remaining);
}

bool IsSafe(const vector<int>& arr, const int skips_remaining) {
    if (skips_remaining < 0) { return false; }
    Trend trend = Trend::Unset;
    for (int i = 0; i < arr.size() - 1; ++i) {
        const int jump = abs(arr[i] - arr[i+1]);
        if (not(1 <= jump && jump <= 3)) {
            return TryWithTwoCandidates(arr, i, skips_remaining-1);
        } else if (arr[i] < arr[i+1]) {
            if (trend == Trend::Unset) { trend = Trend::Increasing; }
            else if (trend == Trend::Decreasing) { return TryWithTwoCandidates(arr, i ,skips_remaining-1); }
        } else if (arr[i] > arr[i+1]) {
            if (trend == Trend::Unset) { trend = Trend::Decreasing; }
            else if (trend == Trend::Increasing) { return TryWithTwoCandidates(arr, i ,skips_remaining-1); }
        }
        // no need to check for equality: the jump check took care of that
    }
    return true;
}

}  // namespace advent2024

int main() {
    ifstream file("2.txt");
    if (!file.is_open()) {
        cerr << "Couldn't open file" << endl;
        return 1;
    }

    vector<vector<int>> data;
    string line;
    while (getline(file, line)) {
        vector<int> row;
        istringstream ss(line);
        int number;
        while (ss >> number) {
            row.push_back(number);
        }
        data.push_back(row);
    }

    int result1 = 0, result2 = 0;
    for (int i = 0; i < data.size(); ++i) {
        if (advent2024::IsSafe(data[i], 0)) { result1++; }
        if (advent2024::IsSafe(data[i], 1)) { result2++; }
    }
    cout << result1 << " " << result2 << endl;

    file.close();
    return 0;
}
