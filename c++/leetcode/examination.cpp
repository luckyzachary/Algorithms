#include <gtest/gtest.h>
#include <vector>
using namespace std;

class Solution {
   public:
    vector<string> findBrother(string& word, string article) {
        int hash = 0;
        vector<string> brothers;
        for (int i = 0; i < word.length(); i++) {
            hash |= 1 << (word[i] - 'a');
        }
        return brothers;
    }
};

int main(int argc, char* argv[]) {
    // testing::InitGoogleTest(&argc, argv);
    // return RUN_ALL_TESTS();
    Solution s;
    s.findBrother("aab", "aab, aac, aad");
}

// TEST(testName, case1) {
//     Solution solution;
//     EXPECT_EQ(1, 1);
// }
