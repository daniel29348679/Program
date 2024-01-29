/*
 * @lc app=leetcode id=88 lang=rust
 *
 * [88] Merge Sorted Array
 */

// @lc code=start
impl Solution {
    pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
        let m = m as usize;
        let n = n as usize;
        let mut v = Vec::new();
        let mut i: usize = 0;
        let mut j: usize = 0;
        while i < m && j < n {
            if nums1[i] < nums2[j] {
                v.push(nums1[i]);
                i += 1;
            } else {
                v.push(nums2[j]);
                j += 1;
            }
        }
        while i < m {
            v.push(nums1[i]);
            i += 1;
        }
        while j < n {
            v.push(nums2[j]);
            j += 1;
        }

        for i in 0..m + n {
            nums1[i] = v[i];
        }
    }
}
// @lc code=end
