<h1>linked_lists</h1>

Compilation of all linked list whiteboarding problems with psuedocode notes and step by step guidance on how I solve each problem.

## Table of Contents

<li><a href="#sortlist">SortList</a></li>
<li><a href="#mergesort">Merge 2 Sorted Lists</a></li>
<li><a href="#removenth">Remove Nth Node from End</a></li>
<li><a href="#misc">Misc Notes</a></li>
</ul>

<a name="sortlist"></a>
## SortList

<p> Time Complexity: O(nlogn) </p>
<p> Space Complexity O(n)</p>

1) identify dummy head/current pointer
2) check if lists exist/have content within. if either are empty, return the other.
4) sort into merged list by comparing left and right. 
5) return dummy.next to give entire list

<a name="llist_cycle"></a>
## Determine if Cycle Present

<p> Time Complexity: O(nlogn) </p>
<p> Space Complexity O(n)</p>

1) identify dummy head/current pointer
2) check if lists exist/have content within. if either are empty, return the other.
4) sort into merged list by comparing left and right. 
5) return dummy.next to give entire list

<a name="mergesort"></a>
## Merge 2 Sorted Lists

<p> Time Complexity: O(nlogn) </p>
<p> Space Complexity O(n)</p>
<p> Resource/Tutorial: https://www.youtube.com/watch?v=y1RnweT17v0 </p>

1) Find the midpoint (utilize slow,fast method; assign mid to slow.next
2) identify left and right lists (slow.next = head of right list)
3) recurse sortList thru left and right list (continue identifying mids, sort, merge thru each recursed level)
4) similar to sortList, merge left and right (identify dummy head/current pointer - sort into merged list by comparing left and right. return dummy.next to give entire list

<a name="removenth"></a>
## Remove Nth Node from End

<p> Time Complexity: O(n) in worst case scenario. (if no cycle, O(N/2)). </p>
<p> Space Complexity O(n)</p>
<p> Resource/Tutorial: https://www.youtube.com/watch?v=IwKSscJW0Uk </p>

1) Create dummy head node
2) point "fast" and "slow" both to dummy_head
3) iterate through list, move fast.pointer to fast.next. delay slow pointer's movement by n interations.
4) once fast pointer hits last node, slow.next == node prior to node_to_del
5) reassign slow.next to node_to_del.next
6) delete node_to_del and return head

Summary: use of two pointers (with n-step delay) to determine traits about directional data structures. In this case, used to determine if there are cycles in a data structure (in O(n) time).

<a name="misc"></a>
## Misc Notes
- cannot use quicksort on linked lists bc linked lists are not indexable
- If you only use pointers without any other extra space, the space complexity will be O(1).
