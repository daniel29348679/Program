/*
 * @lc app=leetcode id=13 lang=rust
 *
 * [13] Roman to Integer
 */

// @lc code=start
impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let mut total = 0;
        let mut s = s.chars();
        let mut prev = ' ';
        for c in s {
            if c == 'I' {
                total += 1;
            }
            if c == 'V' {
                if prev == 'I' {
                    total -= 2;
                }
                total += 5;
            }
            if c == 'X' {
                if prev == 'I' {
                    total -= 2;
                }
                total += 10;
            }
            if c == 'L' {
                if prev == 'X' {
                    total -= 20;
                }
                total += 50;
            }
            if c == 'C' {
                if prev == 'X' {
                    total -= 20;
                }
                total += 100;
            }
            if c == 'D' {
                if prev == 'C' {
                    total -= 200;
                }
                total += 500;
            }
            if c == 'M' {
                if prev == 'C' {
                    total -= 200;
                }
                total += 1000;
            }
            prev = c;
        }
        total
    }
}
// @lc code=end
