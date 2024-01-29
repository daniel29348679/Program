/*
 * @lc app=leetcode id=21 lang=rust
 *
 * [21] Merge Two Sorted Lists
 */

// @lc code=start
// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn merge_two_lists(
        mut list1: Option<Box<ListNode>>,
        mut list2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut prehead = ListNode::new(99999);
        let mut cur = &mut prehead.next;
        while list1.is_some() && list2.is_some() {
            let val1 = list1.as_ref().unwrap().val;
            let val2 = list2.as_ref().unwrap().val;
            if val1 < val2 {
                *cur = list1;
                list1 = cur.as_mut().unwrap().next.take();
                println!("list1: {:?}", list1);
            } else {
                *cur = list2;
                list2 = cur.as_mut().unwrap().next.take();
            }
            cur = &mut cur.as_mut().unwrap().next;
        }

        while (list1.is_some()) {
            *cur = list1;
            list1 = cur.as_mut().unwrap().next.take();
            cur = &mut cur.as_mut().unwrap().next;
        }

        while (list2.is_some()) {
            *cur = list2;
            list2 = cur.as_mut().unwrap().next.take();
            cur = &mut cur.as_mut().unwrap().next;
        }

        prehead.next
    }
}
// @lc code=end
