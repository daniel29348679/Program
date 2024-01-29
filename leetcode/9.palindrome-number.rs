/*
 * @lc app=leetcode id=9 lang=rust
 *
 * [9] Palindrome Number
 */

// @lc code=start
impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let mut sum = 0;
        let mut cur = x;
        while cur > 0 {
            sum = sum * 10 + cur % 10;
            cur /= 10;
        }

        sum == x
    }
}
// @lc code=end
