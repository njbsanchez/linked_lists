# linked_lists



<a name="aboutme"></a>
## SortList

1) find mid point


<a name="mergsort"></a>
## Merge 2 Sorted Lists

1) Find the midpoint (utilize slow,fast method; assign mid to slow.next
2) identify left and right lists (slow.next = head of right list)
3) recurse sortList thru left and right list (continue identifying mids, sort, merge thru each recursed level)
4) similar to sortList, merge left and right (identify dummy head/current pointer - sort into merged list by comparing left and right. return dummy.next to give entire list

<p> Time Complexity: O(nlogn) </p>
<p> Space Complexity O(n)</p>
<p> Resource/Tutorial: https://www.youtube.com/watch?v=y1RnweT17v0 </p>


## Sort Notes
- cannot use quicksort on linked lists bc linked lists are not indexable
