/*
 * @lc app=leetcode id=145 lang=rust
 *
 * [145] Binary Tree Postorder Traversal
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
    pub fn postorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut v = Vec::new();
        fn tra(root: Option<Rc<RefCell<TreeNode>>>, v: &mut Vec<i32>) {
            match root {
                None => (),
                Some(n) => {
                    let n = n.borrow();
                    tra(n.left.clone(), v);
                    tra(n.right.clone(), v);
                    v.push(n.val);
                }
            }
        }

        tra(root, &mut v);
        v
    }
}
// @lc code=end
