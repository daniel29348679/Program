/*
 * @lc app=leetcode id=119 lang=rust
 *
 * [119] Pascal's Triangle II
 */

// @lc code=start
impl Solution {
    pub fn get_row(row_index: i32) -> Vec<i32> {
        let mut result = Vec::new();
        result.push(1);
        let row_index = row_index as i64;
        let mut c: i64 = 1;
        for i in 0..row_index {
            c *= row_index - i;
            c /= i + 1;
            result.push(c as i32);
        }
        result
    }
}
// @lc code=end
