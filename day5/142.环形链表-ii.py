#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        s = set()
        cur = head
        while cur.next:
            if cur in s:
                return cur
            else:
                s.add(cur)
                cur = cur.next
        return None


# @lc code=end
