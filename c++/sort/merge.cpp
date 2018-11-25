#define TEST_TIMES 100
#include <gtest/gtest.h>
#include <cstdlib>
#include <vector>
#include "../tools.cpp"
using namespace std;

vector<int> mergeSort(vector<int> &iArr, vector<int> &tmpArr, int left, int right) {
    if (left >= right) {
        return iArr;
    }
    int middle = (left + right) / 2;
    mergeSort(iArr, tmpArr, left, middle);
    mergeSort(iArr, tmpArr, middle + 1, right);
    for (int i = 0; i <= middle - left; i++) {
        tmpArr[left + i] = iArr[left + i];
        tmpArr[middle + 1 + i] = iArr[right - i];
    }
    int l = left;
    int r = right;
    int index = left;
    while (index <= right) {
        iArr[index++] = tmpArr[l] <= tmpArr[r] ? tmpArr[l++] : tmpArr[r--];
    }
    return iArr;
};

int main(int argc, char *argv[]) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

TEST(testMergeSort, TEST_TIMES) {
    auto iArrMod = initData(TEST_TIMES);
    sort(iArrMod.begin(), iArrMod.end());
    auto sortedArr = iArrMod;
    vector<int> tmpArr;
    tmpArr.reserve(iArrMod.size());
    for (int i = 0; i < TEST_TIMES; i++) {
        random_shuffle(iArrMod.begin(), iArrMod.end());
        auto result = mergeSort(iArrMod, tmpArr, 0, iArrMod.size() - 1);
        EXPECT_EQ(result, sortedArr);
    }
}
