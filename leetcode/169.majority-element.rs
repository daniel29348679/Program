/*
 * @lc app=leetcode id=169 lang=rust
 *
 * [169] Majority Element
 */

// @lc code=start
impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut maj = 0;
        let mut count = 0;

        for i in nums {
            if count == 0 {
                maj = i;
            }

            if maj == i {
                count += 1;
            } else {
                count -= 1;
            }
        }

        maj
    }
}
// @lc code=end
