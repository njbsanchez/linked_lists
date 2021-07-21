# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = dummy
        if l1 == None and l2 == None:
            return None
        elif l1 == None and l2 != None:
            return l2
        elif l2 != None and l2 == None:
            return l1

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                cur = l1
                l1 = cur.next
            else:
                cur.next = l2
                cur = l2                # remember to move
                l2 = cur.next
        if not l1:
            cur.next = l2
        if not l2:
            cur.next = l1
        
        return dummy.next
    
#     # set dummy pointer to a dummy head node
#     # sedfadt a "current" pointer to dummy head
#     # if l1 == None and l2 == None:
#         # return None
#     # elif l1 == None and l2 != None:
#         # return l2
#     #elif l1 != None and l2 == None:
#         # return l1
#     #else:
#         #while l1 and l2 are != None:
#             # if l1 < l2:
#                 #cur.next = l1
#                 #l1 = l1.next
#             # else
#                 #cur.next = l2
#                 #l2 = l2.next
#             #cur = cur.next    
#         #if not l1:
#             cur.next = l2
#         #if not l2:
#             cur.next = l2
            
    