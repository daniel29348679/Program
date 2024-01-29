/*
 * @lc app=leetcode id=58 lang=rust
 *
 * [58] Length of Last Word
 */

// @lc code=start
impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        s.trim_end().chars().rev().take_while(|x| *x != ' ').count() as i32
    }
}
// @lc code=end
