/*
 * @lc app=leetcode id=121 lang=rust
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let (mut mi, mut ma) = (999999, 0);
        for i in prices {
            ma = std::cmp::max(ma, i - mi);
            mi = std::cmp::min(mi, i);
        }
        ma
    }
}
// @lc code=end
