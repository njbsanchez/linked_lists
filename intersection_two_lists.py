"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.


"""
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a = headA
        b = headB
        while a != b:
            if a:
                a = a.next 
            else:
                a = headB
            if b:
                b = b.next
            else:
                b = headA
        return a
                
"""
Length of list headA = L1 + K (L1 = length of nodes unique to headA; K = length of shared nodes)
Length of list headB = L2 + k (L2 = length of nodes unique to headB; K = length of shared nodes)

to find start of converging nodes with list b - pointer of list a would need to transverse through entire A and B (L1 + K + L2)
to find start of converging nodes with list A - pointer of list a would need to transverse through entire B and A (L2 + K + L1)

both would arrive at start of K

Time Complexity - O(2(L1 + L2 + K))
Space Complexity - O(1)

"""