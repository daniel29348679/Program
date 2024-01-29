/*
 * @lc app=leetcode id=118 lang=rust
 *
 * [118] Pascal's Triangle
 */

// @lc code=start
impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        let mut result = Vec::new();
        let mut n = Vec::new();
        for i in 0..num_rows {
            for j in (1..i).rev() {
                n[j as usize] += n[(j - 1) as usize];
            }
            n.push(1);
            result.push(n.clone())
        }
        result
    }
}
// @lc code=end
