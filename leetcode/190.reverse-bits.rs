/*
 * @lc app=leetcode id=190 lang=rust
 *
 * [190] Reverse Bits
 */

// @lc code=start
impl Solution {
    pub fn reverse_bits(x: u32) -> u32 {
        let mut sum = 0;
        for i in 0..32 {
            if x & (1 << i) > 0 {
                sum = sum | 1 << (31 - i);
            }
        }

        sum
    }
}
// @lc code=end
