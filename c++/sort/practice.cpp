#define TEST_TIMES 100
#include <gtest/gtest.h>
#include <cstdlib>
#include <vector>
#include "../tools.cpp"
using namespace std;

vector<int> sort1(vector<int> &iArr) {
    
    return iArr;
};

int main(int argc, char *argv[]) {
    int i = 0;
    int j = 1;
    cout << (i < j ? i-- : j++) << endl;
    cout << i << " " << j << endl;

    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

TEST(testSort1, TEST_TIMES) {
    auto iArrMod = initData(TEST_TIMES);
    sort(iArrMod.begin(), iArrMod.end());
    auto sortedArr = iArrMod;
    for (int i = 0; i < TEST_TIMES; i++) {
        random_shuffle(iArrMod.begin(), iArrMod.end());
        auto result = sort1(iArrMod);
        EXPECT_EQ(result, sortedArr);
    }
}
