/*
 * @lc app=leetcode id=168 lang=rust
 *
 * [168] Excel Sheet Column Title
 */

// @lc code=start
impl Solution {
    pub fn convert_to_title(column_number: i32) -> String {
        let mut s = String::new();
        let mut column_number = column_number;
        while column_number > 0 {
            column_number -= 1;
            let ch = ((column_number % 26) as u8) + b'A';
            s.insert(0, ch as char);
            column_number /= 26;
        }

        s
    }
}
// @lc code=end
