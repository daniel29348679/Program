/*
 * @lc app=leetcode id=26 lang=rust
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut total = 0;
        let mut prev = -200;
        for i in 0..nums.len() {
            if nums[i] != prev {
                if i != total {
                    nums[total] = nums[i];
                }
                total += 1;
                prev = nums[i];
            }
        }

        total as i32
    }
}
// @lc code=end
