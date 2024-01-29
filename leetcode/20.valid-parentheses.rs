/*
 * @lc app=leetcode id=20 lang=rust
 *
 * [20] Valid Parentheses
 */

// @lc code=start
impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut v = Vec::new();
        for ch in s.chars() {
            if ch == '(' || ch == '[' || ch == '{' {
                v.push(ch);
                continue;
            }
            if ch == ')' {
                match v.pop() {
                    None => return false,
                    Some(c) => {
                        if c != '(' {
                            return false;
                        }
                    }
                }
            }
            if ch == ']' {
                match v.pop() {
                    None => return false,
                    Some(c) => {
                        if c != '[' {
                            return false;
                        }
                    }
                }
            }
            if ch == '}' {
                match v.pop() {
                    None => return false,
                    Some(c) => {
                        if c != '{' {
                            return false;
                        }
                    }
                }
            }
        }

        v.is_empty()
    }
}
// @lc code=end
