#include <gtest/gtest.h>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
   public:
    bool isBalanced(TreeNode *root) { return getDepth(root) != -1; }
    int getDepth(TreeNode *root) {
        if (root == NULL) {
            return 0;
        }

        int l = getDepth(root->left);
        if (l == -1) {
            return -1;
        }
        int r = getDepth(root->right);
        if (r == -1) {
            return -1;
        }
        if (abs(l - r) > 1) {
            return -1;
        }
        return max(l, r) + 1;
    }
};

int main(int argc, char *argv[]) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

TEST(testName, case1) {
    Solution solution;
    EXPECT_EQ(1, 1);
}
