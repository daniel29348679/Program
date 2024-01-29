/*
 * @lc app=leetcode id=69 lang=rust
 *
 * [69] Sqrt(x)
 */

// @lc code=start
impl Solution {
    pub fn my_sqrt(x: i32) -> i32 {
        let target = x as i64;
        let mut left: i64 = 0;
        let mut right: i64 = 2 << 16;
        while left < right {
            let mid = (left + right) / 2;
            if mid * mid <= target && (mid + 1) * (mid + 1) > target {
                return mid as i32;
            } else if mid * mid > target {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left as i32;
    }
}
// @lc code=end
