/*
 * @lc app=leetcode id=171 lang=rust
 *
 * [171] Excel Sheet Column Number
 */

// @lc code=start
impl Solution {
    pub fn title_to_number(column_title: String) -> i32 {
        column_title
            .bytes()
            .into_iter()
            .map(|x| (x - b'A' + 1) as i32)
            .fold(0, |sum, cur| sum * 26 + cur)
    }
}
// @lc code=end
