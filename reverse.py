# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def iterReverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        if head or head.next does not exist,
        return head
        
        assign head as "done"
        assign head.next as "current"
        
        point done.next to None
        
        1>none>2>3>4>none
        d       c
        
        while cur exists:
            assign current.next as "hold"
            move current before "done" (2>1>none 3>4>none)
            reassign current as "done"
            reassign hold as "current"
        
        """
        
        if head is None or head.next is None:
            return head
        
        done = head
        current = head.next
        done.next = None
        
        while current:
            hold = current.next
            current.next = done
            
            done = current
            current = hold
        
        return done
    
     def recurseReverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        if head or head.next does not exist,
        return head
        
        implement recursion of recurseReverseList to identify new head node (last node in list) and start reversing beginning at new head node.
        
        point done.next to None
        
        1>none>2>3>4>none
        d       c
        
        while cur exists:
            assign current.next as "hold"
            move current before "done" (2>1>none 3>4>none)
            reassign current as "done"
            reassign hold as "current"
        
        """
        
        if not head or not head.next:
            return head
        second = head.next
        reverse = self.recurseReverseList(second)
        second.next = head
        head.next = None
        
        return reverse
    
