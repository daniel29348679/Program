/*
 * @lc app=leetcode id=28 lang=rust
 *
 * [28] Find the Index of the First Occurrence in a String
 */

// @lc code=start
impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        if haystack.len() < needle.len() {
            return -1 as i32;
        }
        let hay = haystack.as_bytes();
        let ndl = needle.as_bytes();

        for i in 0..hay.len() - ndl.len() + 1 {
            let mut found = true;
            for j in 0..ndl.len() {
                if hay[i + j] != ndl[j] {
                    found = false;
                    break;
                }
            }
            if found {
                return i as i32;
            }
        }

        -1 as i32
    }
}
// @lc code=end
