#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1, l2 = headB, headA

        while l1 != l2:
            l1 = headA if l1 is None else l1.next
            l2 = headB if l2 is None else l2.next
        return l1

# @lc code=end
