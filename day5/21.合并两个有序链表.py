#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 is None:
            return l2
        if l2 is None:
            return l1
        preNode = ListNode(-1)
        pre = preNode
        while l1 and l2:
            if l1.val <= l2.val:
                pre.next = l1
                l1 = l1.next

            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next

        pre.next = l1 if l1 is not None else l2
        return preNode.next
        
    

# @lc code=end
