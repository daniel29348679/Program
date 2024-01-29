/*
 * @lc app=leetcode id=66 lang=rust
 *
 * [66] Plus One
 */

// @lc code=start
impl Solution {
    pub fn plus_one(mut digits: Vec<i32>) -> Vec<i32> {
        let mut carry = 1;
        digits.iter_mut().rev().for_each(|x| {
            carry += *x;
            *x = carry % 10;
            carry /= 10;
        });
        if carry > 0 {
            digits.insert(0, carry);
        }

        digits
    }
}
// @lc code=end
