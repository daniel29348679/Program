/*
 * @lc app=leetcode id=2 lang=javascript
 *
 * [2] Add Two Numbers
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
	var head = new ListNode();
	var cur = head;
	var carry = 0;
	while (l1 != null || l2 != null || carry != 0) {
		if (l1 != null) {
			carry += l1.val;
			l1 = l1.next;
		}
		if (l2 != null) {
			carry += l2.val;
			l2 = l2.next;
		}
		cur.val = carry % 10;
		carry = parseInt(carry / 10);
		if (l1 != null || l2 != null || carry != 0) {
			cur.next = new ListNode();
			cur = cur.next;
		}
	}
	return head;
};
// @lc code=end
