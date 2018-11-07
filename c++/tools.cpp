#include <gtest/gtest.h>
#include <iostream>
#include <vector>
using namespace std;

template <class T>
void printArray(vector<T> array) {
    cout << "[ ";
    copy(array.begin(), array.end(), ostream_iterator<T>(cout, ", "));
    cout << "] \n";
}

vector<int> initData(int count) {
    vector<int> array;
    for (int i = 0; i < count; i++) {
        array.push_back(rand());
    }
    return array;
}
