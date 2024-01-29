/*
 * @lc app=leetcode id=9 lang=javascript
 *
 * [9] Palindrome Number
 */

// @lc code=start
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
	var str = x.toString();
	if (str[0] == "-") return false;
	for (var i = 0; i < str.length / 2; i++) {
		if (str[i] != str[str.length - 1 - i]) return false;
	}
};
// @lc code=end
