/*
 * @lc app=leetcode id=67 lang=rust
 *
 * [67] Add Binary
 */

// @lc code=start
impl Solution {
    pub fn add_binary(a: String, b: String) -> String {
        let aa = a.chars().rev().collect::<Vec<char>>();
        let bb = b.chars().rev().collect::<Vec<char>>();
        let mut result = String::new();
        let mut carry = 0;
        for i in 0..std::cmp::max(aa.len(), bb.len()) {
            if i < aa.len() {
                carry += aa[i] as i32 - '0' as i32;
            }
            if i < bb.len() {
                carry += bb[i] as i32 - '0' as i32;
            }
            if carry % 2 == 0 {
                result.push('0');
            } else {
                result.push('1');
            }
            carry /= 2;
        }
        if carry > 0 {
            result.push('1');
        }

        result.chars().rev().collect::<String>()
    }
}
// @lc code=end
