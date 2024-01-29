/*
 * @lc app=leetcode id=111 lang=rust
 *
 * [111] Minimum Depth of Binary Tree
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
    pub fn min_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        match root {
            None => 0,
            Some(ro) => {
                let mut r = Self::min_depth(ro.borrow().right.clone());
                let mut l = Self::min_depth(ro.borrow().left.clone());
                if r == 0 && l == 0 {
                    1
                } else {
                    if r == 0 {
                        r = 9999;
                    }
                    if l == 0 {
                        l = 9999;
                    }
                    std::cmp::min(r, l) + 1
                }
            }
        }
    }
}
// @lc code=end
