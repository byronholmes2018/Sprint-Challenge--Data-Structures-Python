"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        if(self.head == None):
            self.head = ListNode(value, prev=None, next=None)
            self.tail = self.head
        else:
            old_head = self.head
            old_head.prev = ListNode(value, prev=None, next=old_head)
            self.head = old_head.prev

    def remove_from_head(self):
        if(self.head is None):
            return None
        if(self.head != None and self.head.next):
            old_head = self.head
            self.head = old_head.next
            self.head.prev = None
        else:
            old_head = self.head
            self.head = None
            self.tail = None
        return old_head.value

    def add_to_tail(self, value):
        if(self.tail):
            new_node = ListNode(value, prev=self.tail, next=None)
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = ListNode(value, prev=None, next=None)
            self.tail = self.head

    def remove_from_tail(self):
        if(self.tail.prev):
            old_tail = self.tail
            new_tail = old_tail.prev
            new_tail.next = None
            self.tail = new_tail
        else:
            old_tail = self.tail
            self.head = None
            self.tail = None
        return old_tail.value

    def move_to_front(self, node):
        if node.prev is None:
            return
        if node.next:
            node.prev.next = node.next
            node.next.prev = node.prev

        old_head = self.head
        old_head.prev = node
        node.next = old_head
        node.prev = None
        self.head = node
        print('moving to front')
        print('old head', old_head, 'old head next', old_head.next, 'old head prev', old_head.prev)
        print('new head', self.head, 'new head next', self.head.next, 'new head prev', self.head.prev)

    def move_to_end(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        old_tail = self.tail
        old_tail.next = node
        node.next = None
        node.prev = old_tail
        self.tail = node

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

    def get_max(self):
        max_value = self.head.value
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
            if current_node.value > max_value:
                max_value = current_node.value
        return max_value

class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, item):
        self.storage.add_to_tail(item)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()  

    def len(self):
        return self.size



class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
    




    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
          return True
        if target < self.value:
          if not self.left:
            return False
          else:
            return self.left.contains(target)
        
        else:
          if not self.right:
            return False
          else:
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        max = 0
        next = self
        while(next):
          if next.value > max:
            max = next.value
          next = next.right
        return max

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        queue = Queue()
        if self.left is not None:
          queue.enqueue(self.left)
        if self.right is not None:
          queue.enqueue(self.right)
        while(queue.len() > 0):
          node_to_eval = queue.dequeue()
          cb(node_to_eval.value)
          if node_to_eval.left is not None:
            queue.enqueue(node_to_eval.left)
          if node_to_eval.right is not None:
            queue.enqueue(node_to_eval.right)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
      stack = Stack()
      stack.push(self)  
      if self.left is None:
        value = stack.pop()
        print(value.value)
        if self.right is None:
          return
        else:
          self.in_order_print(self.right)
      else:
          self.in_order_print(self.left)
  

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        print(self.value)
        queue = Queue()
        if self.left is not None:
          queue.enqueue(self.left)
        if self.right is not None:
          queue.enqueue(self.right)
        while(queue.len() > 0): 
          node_to_eval = queue.dequeue()
          print(node_to_eval.value)
          if node_to_eval.left is not None:
            queue.enqueue(node_to_eval.left)
          if node_to_eval.right is not None:
            queue.enqueue(node_to_eval.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        print(self.value)
        stack = Stack()
        if self.left is not None:
          stack.push(self.left)
        if self.right is not None:
          stack.push(self.right)
        while(stack.len() > 0):
          node_to_eval = stack.pop()
          print(node_to_eval.value)
          if node_to_eval.left is not None:
            stack.push(node_to_eval.left)
          if node_to_eval.right is not None:
            stack.push(node_to_eval.right)
import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
duplicates = []
bst = BinarySearchTree(names_1[0])
for name in names_1[1:]:
   print(name)
   bst.insert(name)

for name in names_2:
    if bst.contains(name):
        duplicates.append(name)
    
'''
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

