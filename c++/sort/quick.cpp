#define TEST_TIMES 100
#include <gtest/gtest.h>
#include <cstdlib>
#include <vector>
#include "../tools.cpp"
using namespace std;

vector<int> quickSort1(vector<int> &iArr, int left, int right) {
    if (left >= right) {
        return iArr;
    }
    int lt = left;
    int gt = right;
    while (lt < gt) {
        while (iArr[lt] <= iArr[gt] && lt < gt) {
            lt++;
        }
        swap(iArr[lt], iArr[gt]);
        while (iArr[gt] >= iArr[lt] && lt < gt) {
            gt--;
        }
        swap(iArr[lt], iArr[gt]);
    }
    quickSort1(iArr, left, lt - 1);
    quickSort1(iArr, lt + 1, right);
    return iArr;
}

vector<int> quickSort2(vector<int> &iArr, int left, int right) {
    if (left >= right) {
        return iArr;
    }
    int lt = left;
    int gt = right;
    int tmp = iArr[right];
    while (lt < gt) {
        while (iArr[lt] <= tmp && lt < gt) {
            lt++;
        }
        iArr[gt] = iArr[lt];
        while (iArr[gt] >= tmp && lt < gt) {
            gt--;
        }
        iArr[lt] = iArr[gt];
    }
    iArr[lt] = tmp;
    quickSort2(iArr, left, lt - 1);
    quickSort2(iArr, lt + 1, right);
    return iArr;
}

vector<int> quickSort3(vector<int> &iArr, int left, int right) {
    if (left >= right) {
        return iArr;
    }

    int pivot = left;
    for (int i = left; i < right; i++) {
        if (iArr[i] < iArr[right]){
            swap(iArr[pivot++], iArr[i]);
        }
    }
    swap(iArr[pivot], iArr[right]);
    quickSort3(iArr, left, pivot - 1);
    quickSort3(iArr, pivot + 1, right);
    return iArr;
}

int main(int argc, char *argv[]) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

TEST(testQuickSort1, TEST_TIMES) {
    auto iArrMod = initData(TEST_TIMES);
    sort(iArrMod.begin(), iArrMod.end());
    auto sortedArr = iArrMod;
    for (int i = 0; i < TEST_TIMES; i++) {
        random_shuffle(iArrMod.begin(), iArrMod.end());
        auto result = quickSort1(iArrMod, 0, iArrMod.size() - 1);
        EXPECT_EQ(result, sortedArr);
    }
}

TEST(testQuickSort2, TEST_TIMES) {
    auto iArrMod = initData(TEST_TIMES);
    sort(iArrMod.begin(), iArrMod.end());
    auto sortedArr = iArrMod;
    for (int i = 0; i < TEST_TIMES; i++) {
        random_shuffle(iArrMod.begin(), iArrMod.end());
        auto result = quickSort2(iArrMod, 0, iArrMod.size() - 1);
        EXPECT_EQ(result, sortedArr);
    }
}

TEST(testQuickSort3, TEST_TIMES) {
    auto iArrMod = initData(TEST_TIMES);
    sort(iArrMod.begin(), iArrMod.end());
    auto sortedArr = iArrMod;
    for (int i = 0; i < TEST_TIMES; i++) {
        random_shuffle(iArrMod.begin(), iArrMod.end());
        auto result = quickSort3(iArrMod, 0, iArrMod.size() - 1);
        EXPECT_EQ(result, sortedArr);
    }
}