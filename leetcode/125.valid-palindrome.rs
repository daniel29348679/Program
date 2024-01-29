/*
 * @lc app=leetcode id=125 lang=rust
 *
 * [125] Valid Palindrome
 */

// @lc code=start
impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let a = s.chars();
        let mut v = Vec::new();
        for c in a {
            if 'a' <= c && c <= 'z' {
                v.push(c);
            }
            if 'A' <= c && c <= 'Z' {
                v.push(c);
            }
            if '0' <= c && c <= '9' {
                v.push(c);
            }
        }
        let mut ans = true;
        v.iter()
            .zip(v.iter().rev())
            .all(|(x, y)| x.to_ascii_lowercase() == y.to_ascii_lowercase())
    }
}
// @lc code=end
