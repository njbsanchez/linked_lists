class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
        
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return None
                
        new_node.next = self.head
        self.head = new_node
        
        return None
    
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        self.tail.next = new_node
        self.tail = self.tail.next
        
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        
        new_node = Node(val)
        counter = 0
        cur_node = self.head
        while cur_node:
            if counter == index: 
                new_node.next = cur_node.next
                cur_node.next = new_node
            cur_node = cur_node.next
            counter += 1
                
        return None
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """

        ind_before = 1
        cur_node = self.head
        
        while cur_node:
            print(cur_node.data)
            print(ind_before)
            if ind_before == index:
               print("at index")
               to_delete = cur_node.next
               cur_node.next = to_delete.next
               return
            cur_node = cur_node.next
            ind_before += 1
            print("***")
                
        return None   


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

llist = MyLinkedList()
llist.addAtTail("A")
llist.addAtTail("B")
llist.addAtTail("C")
llist.addAtTail("D")
llist.addAtHead("AA")
llist.addAtIndex(3, "E")