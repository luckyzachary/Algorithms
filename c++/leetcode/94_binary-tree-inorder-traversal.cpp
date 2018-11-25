#include <gtest/gtest.h>
#include <vector>
using namespace std;
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
   public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> values = vector<int>();
        if (root == NULL) {
            return values;
        }
        vector<TreeNode*> stack;
        TreeNode* node = root;
        stack.push_back(node);
        while (!stack.empty()) {
            while (node->left != NULL) {
                stack.push_back(node);
                node = node->left;
            }
            while (stack.back()->right == NULL) {
                int value = stack.back()->val;
                values.push_back(value);
                stack.pop_back();
            }
            TreeNode* node = stack.back();
            values.push_back(node->val);
            stack.back();
            node = node->right;
            stack.push_back(node);
        }
        return values;
    }
};

int main(int argc, char* argv[]) {
    // testing::InitGoogleTest(&argc, argv);
    // return RUN_ALL_TESTS();
    TreeNode tn1 = TreeNode(1);
    TreeNode tn2 = TreeNode(2);
    TreeNode tn3 = TreeNode(3);
    tn1.right = &tn2;
    tn2.left = &tn3;
    Solution solution;
    solution.inorderTraversal(&tn1);
    return 0;
}

// TEST(testName, case1) {
//     TreeNode tn1 = TreeNode(1);
//     TreeNode tn2 = TreeNode(2);
//     TreeNode tn3 = TreeNode(3);
//     tn1.right = &tn2;
//     tn2.left = &tn3;
//     Solution solution;
//     vector<int> except = vector<int>{1, 3, 2};
//     EXPECT_EQ(solution.inorderTraversal(&tn1), except);
// }
