#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        thead = ListNode(-1)
        thead.next = head
        pre, cur = None, thead
        while cur:
            pre = cur
            cur = cur.next

            while cur and cur.next and cur.val == cur.next.val:
                t = cur.val
                while cur and cur.val == t:
                    cur = cur.next
            pre.next = cur
        return thead.next

# @lc code=end
