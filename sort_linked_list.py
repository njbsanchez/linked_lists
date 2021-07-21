#tutorial - https://www.youtube.com/watch?v=y1RnweT17v0



class ListNode(object):
    """ Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        """
        identify mid
        """
        if not head or not head.next:
            return head
        mid = self.midPoint(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
        
    def midPoint(self, head):
        """splits linked list in left and right side"""
        slow,fast = head,head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid

    def merge(self, left, right):
        dummy = cur = ListNode(0)
        while left and right:
            if left.val < right.val:
                cur.next = left
                cur = cur.next
                left = left.next
            else:
                cur.next = right
                cur = cur.next
                right = right.next
        cur.next = left or right
        return dummy.next