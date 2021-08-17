<h1>linked_lists</h1>

Compilation of all linked list whiteboarding problems with psuedocode notes and step by step guidance on how I solve each problem. 

## Table of Contents

<li><a href="#sortlist">SortList</a></li>
<li><a href="#mergesort">Merge 2 Sorted Lists</a></li>
<li><a href="#llist_cycle">Check for Cycle</a></li>
<li><a href="#removenth">Remove Nth Node from End</a></li>
<li><a href="#reverse">Reverse Linked List (iteratively & recursively)</a></li>
<li><a href="#misc">Misc Notes</a></li>
</ul>

<a name="sortlist"></a>
## SortList

<p><a href="https://github.com/njbsanchez/linked_lists/blob/main/sort_linked_list.py">Code</a></p>
<p>Time Complexity: O(nlogn) </p>
<p> Space Complexity O(n)</p>

1) BASE - check if lists exist/have content within. if either are empty, return the other.
2) mid - find midpoint of the list.
3) split - use slow/fast method & mid to split into two lists. 
4) sort -
    - recursion - sortList will continue to split list down, creates stack of mini lists to compare.
    - merge - return of merge will close out recursion level and merge two sorted lists
5) return self.merge to return final merge of two sorted lists.

<a name="mergesort"></a>
## Merge 2 Sorted Lists

<p><a href="https://github.com/njbsanchez/linked_lists/blob/main/merge_lists.py">Code</a></p>
<p> Time Complexity: O(nlogn) </p>
<p> Space Complexity O(n)</p>
<p> Resource/Tutorial: https://www.youtube.com/watch?v=y1RnweT17v0 </p>

1)  create dummy node to connect new list to
2)  compare head of l1 and l2; which ever lesser than, assign variable "current" to add to dummy_nodes's linked list. continue with rest of l1 and l2
    - be sure to cover all cases: base case (l1 & l2 == None), if list 1 or list 2 are empty, etc.

<a name="llist_cycle"></a>
## Determine if Cycle Present

<p><a href="https://github.com/njbsanchez/linked_lists/blob/main/two_pointer.py">Code</a></p>
<p> Time Complexity: O(nlogn) </p>
<p> Space Complexity O(n)</p>

1) utilize slow-fast method (assign slow & fast to head)
2) while both fast and fast.next exist, reassign fast and slow to next node in their respective algorithmic pattern
3) return true if fast == slow (variables will eventually point to the same node if there is a cycle). return false if else. (if there is no cycle, fast.next == None)

(To find first node in cycle)

1) utilize slow-fast method (assign slow & fast to head)
2) while both fast and fast.next exist, reassign fast and slow to next node in their respective algorithmic pattern
3) break if fast == slow (variables will eventually point to the same node if there is a cycle. It would have taken 1 1/2 x [length pre-cycle + 1 cycle] for fast == slow). return None if else. (if there is no cycle, fast.next == None)
4) need to go another 1/2 [length of pre-cycle + 1 cycle] to get to starting node of cycle. move head to head.next and slow to slow.next until slow == head. return head.


<a name="removenth"></a>
## Remove Nth Node from End

<p><a href="https://github.com/njbsanchez/linked_lists/blob/main/remove_nth_from_end.py">Code</a></p>
<p> Time Complexity: O(n) in worst case scenario. (if no cycle, O(N/2)). </p>
<p> Space Complexity O(n)</p>
<p> Resource/Tutorial: https://www.youtube.com/watch?v=IwKSscJW0Uk </p>

1) Create dummy head node
2) use n-step delay: point "fast" and "slow" both to dummy_head
3) iterate through list, move fast.pointer to fast.next. delay slow pointer's movement by n interations.
4) once fast pointer hits last node, slow.next == node prior to node_to_del
5) reassign slow.next to node_to_del.next
6) delete node_to_del and return head

Summary: use of two pointers (with n-step delay) to determine traits about directional data structures. In this case, used to determine if there are cycles in a data structure (in O(n) time).

<a name="reverse"></a>
## Reverse Linked List (iteratively)

<p><a href="https://github.com/njbsanchez/linked_lists/blob/main/reverse.py">Code</a></p>
<p> Time Complexity: O(n)</p>
<p> Space Complexity O(n)</p>
<p> Resource/Tutorial: Leetcode </p>

1) base case: if head or head.next does not exist, return head
2) assign head as "done" and head.next as "current"
3) point done.next to None
4) while current still exists, assign current.next as "hold". in the mean time, assign "done" to current.next. reassign "current" to "done".
5) reassign "hold" to "current". 

## Reverse Linked List (recursively)

<p><a href="https://github.com/njbsanchez/linked_lists/blob/main/reverse.py">Code</a></p>
<p> Time Complexity: O(n)</p>
<p> Space Complexity O(n)</p>
<p> Resource/Tutorial: Leetcode </p>

1) assign "current" variable to head
2) base case: if current or current.next does not exist, return current
3) assign hold to current.next
4) recursion - assign "new_head" to self.recurseReverseList(hold) 
    - this puts nodes into an imaginary "stack", which then returns the last node and assigns it to "new_head" variable
    - new_head is returned (last node), next node in "stack" is assigned to new_head.next
    - new_head is returned (the last node), the next node in "stack" is assigned to new_head.next.next and so one until "stack" is cleared.
    - new_head is finally returned, closing out totality of method.

<a name="misc"></a>
## Misc Notes
- cannot use quicksort on linked lists bc linked lists are not indexable
- If you only use pointers without any other extra space, the space complexity will be O(1).
