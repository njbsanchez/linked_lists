# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        """
        create dummy head node (since backward from end does not have an index of 0)
        
        point fast to dummy head
        point slow to dummy head
        
        iterate through list - while fast.next:
            move fast pointer to fast.next
            delay slow pointer by n nodes by reducing n by 1 every iteration till n == 0
                once n == 0: move slow pointer to slow.next
        
        once fast pointer hits last node, slow.next will point to node before node to delete
            mark slow.next as node_to_delete
            reassign slow.next to node after node_to_delete (node_to_del.next)
            delete node_to_del
            
        return head 
        
        """
        
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        fast,slow = dummy_head,dummy_head
        
        while fast.next:
            fast = fast.next
            if n <= 0:
                slow = slow.next
            
            n -= 1
        
        node_to_del = slow.next
        slow.next = node_to_del.next
        
        del node_to_del
            
        return dummy_head.next
    
        """uses Floyd's Cycle Detection algorythm - use of two pointers to determin traits about directional data structures. 
        Use cases:
            - find median in a list using O(n) time complexity
            - (in this case)to determine if there are cuycles in a data structure. 
            
        """