#include <gtest/gtest.h>
#include <vector>
using namespace std;

class Solution {
   public:
    vector<int> sortArrayByParity(vector<int> &A) {
        int i = 0, j = A.size() - 1;
        while (i < j) {
            while (A[i] % 2 == 0 && i < A.size()) i++;
            while (A[j] % 2 == 1 && j >= 0) j--;
            if (i < j) {
                swap(A[i], A[j]);
            }
        }
        return A;
    }
};

int main(int argc, char *argv[]) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

TEST(testName, case1) {
    Solution solution;
    vector<int> A = vector<int>{2, 4, 1, 3};
    EXPECT_EQ(solution.sortArrayByParity(A), A);
}
