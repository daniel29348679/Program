/*
 * @lc app=leetcode id=112 lang=rust
 *
 * [112] Path Sum
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
    pub fn has_path_sum(root: Option<Rc<RefCell<TreeNode>>>, target_sum: i32) -> bool {
        fn travel(root: Option<Rc<RefCell<TreeNode>>>, sum: &mut i32) -> bool {
            match root {
                None => false,
                Some(ro) => {
                    let ro = ro.borrow();
                    *sum -= ro.val;
                    if *sum == 0 && ro.left.is_none() && ro.right.is_none() {
                        *sum += ro.val;
                        return true;
                    }
                    let bo = travel(ro.left.clone(), sum) || travel(ro.right.clone(), sum);
                    *sum += ro.val;
                    bo
                }
            }
        }
        let mut sum = target_sum;
        travel(root, &mut sum)
    }
}
// @lc code=end
