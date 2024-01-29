/*
 * @lc app=leetcode id=94 lang=rust
 *
 * [94] Binary Tree Inorder Traversal
 */

// @lc code=start
// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut v = Vec::new();

        fn dfs(root: Option<Rc<RefCell<TreeNode>>>, v: &mut Vec<i32>) {
            if let Some(node) = root {
                dfs(node.borrow().left.clone(), v);
                v.push(node.borrow().val);
                dfs(node.borrow().right.clone(), v);
            }
        }

        dfs(root, &mut v);
        v
    }
}
// @lc code=end
