class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def lastK(self, head: ListNode, k: int):

        cur = head
        pre = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if k < 1:
                pre = pre.next
            k = k - 1

        if count < k:
            return None
        return pre
