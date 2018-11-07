#include <gtest/gtest.h>
#include <vector>
using namespace std;

class Solution {
   public:

};

int main(int argc, char* argv[]) {
   testing::InitGoogleTest(&argc, argv);
   return RUN_ALL_TESTS();
}

TEST(testName, case1) {
   Solution solution;
   EXPECT_EQ(1, 1);
}
