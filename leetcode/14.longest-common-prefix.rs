/*
 * @lc app=leetcode id=14 lang=rust
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        if strs.len() == 0 {
            return String::from("");
        }
        let mut s = strs[0].clone();
        let mut i = s.len();
        for st in strs.iter() {
            if i > st.len() {
                i = st.len();
            }
            for j in (0..i) {
                if s.chars().nth(j).unwrap() != st.chars().nth(j).unwrap() {
                    i = j;
                    break;
                }
            }
        }
        s[0..i].to_string()
    }
}
// @lc code=end
