/*
 * @lc app=leetcode id=27 lang=rust
 *
 * [27] Remove Element
 */

// @lc code=start
impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut total = 0;
        for i in 0..nums.len() {
            if nums[i] != val {
                if i != total {
                    nums[total] = nums[i];
                }
                total += 1;
            }
        }

        total as i32
    }
}
// @lc code=end
