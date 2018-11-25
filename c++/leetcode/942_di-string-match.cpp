#include <gtest/gtest.h>
#include <vector>
using namespace std;

class Solution {
   public:
    vector<int> diStringMatch(string S) {
        vector<int> diString;
        int b = 0;
        int e = S.length();
        for (int i = 0; i < S.length(); i++) {
            diString.push_back(S[i] == 'I' ? b++ : e--);
        }
        diString.push_back(b);
        return diString;
    }
};

int main(int argc, char* argv[]) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

TEST(testName, case1) {
    string s1 = "IDID";
    string s2 = "III";
    string s3 = "DDI";
    vector<int> r1 = {0, 4, 1, 3, 2};
    vector<int> r2 = {0, 1, 2, 3};
    vector<int> r3 = {3, 2, 0, 1};
    Solution solution;
    EXPECT_EQ(solution.diStringMatch(s1), r1);
    EXPECT_EQ(solution.diStringMatch(s2), r2);
    EXPECT_EQ(solution.diStringMatch(s3), r3);
}
