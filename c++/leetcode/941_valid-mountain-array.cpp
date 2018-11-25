#include <gtest/gtest.h>
#include <vector>
using namespace std;

class Solution {
   public:
    bool validMountainArray(vector<int>& A) {
        if (A.size() < 3) {
            return false;
        }
        int index = 0;
        while (index < A.size() - 1 && A[index] < A[index + 1]) {
            index++;
        }
        if (index == 0 || index >= A.size() - 1) {
            return false;
        }
        while (index < A.size() - 1 && A[index] > A[index + 1]) {
            index++;
        }
        return index >= A.size() - 1;
    }
};

int main(int argc, char* argv[]) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

TEST(testName, case1) {
    Solution solution;
    vector<int> t1 = vector<int>{2, 1};
    vector<int> t2 = vector<int>{3, 5, 5};
    vector<int> t3 = vector<int>{0, 3, 2, 1};

    EXPECT_EQ(solution.validMountainArray(t1), false);
    EXPECT_EQ(solution.validMountainArray(t2), false);
    EXPECT_EQ(solution.validMountainArray(t3), true);
}
