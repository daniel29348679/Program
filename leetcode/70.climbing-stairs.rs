/*
 * @lc app=leetcode id=70 lang=rust
 *
 * [70] Climbing Stairs
 */

// @lc code=start
impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        let mut a = 1;
        let mut b = 1;
        for _ in 0..n - 1 {
            let c = b;
            b = a + b;
            a = c;
        }
        b
    }
}
// @lc code=end
