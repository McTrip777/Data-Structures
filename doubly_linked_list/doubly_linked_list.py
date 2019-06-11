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
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    if self.head is None:
      newNode = ListNode(value)
      newNode.prev = None
      self.head = newNode 
    else:
      newNode = ListNode(value)
      self.head.prev = newNode
      newNode.next = self.head
      self.head = newNode
      newNode.prev = None

  def remove_from_head(self):
    cur = self.head
    if cur == self.head and cur is not None:
      if not cur.next:
        cur = None
        self.head = None
        return
      else:
        nxt = cur.next
        cur.next = None
        nxt.prev = None
        cur = None
        self.head = nxt
        return
    else:
      print("Nothing to remove")


  def add_to_tail(self, value):
    if self.head is None:
      newNode = ListNode(value)
      newNode.prev = None
      self.head = newNode 
      self.tail = newNode
    else:
      newNode = ListNode(value)
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = newNode
      newNode.prev = cur
      newNode.next = None
      self.tail = newNode

  def remove_from_tail(self):
    cur = self.tail
    prev = self.tail.prev
    if cur == self.tail and cur is not None:
      if not cur.next:
        cur.prev = None
        self.tail = None
        prev.next = None
        return
    else:
      print("Nothing to remove")


  def move_to_front(self, node):
    # cur = self.head
    # prv = node.prev
    # nxt = node.next
    # while cur:
    #   if cur == self.node:
    #     prv.next = nxt
    #     nxt.prev = prv
    #   else:
    #     print('something went wrong')
    #   cur = cur.next

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
    
  def get_max(self):
    pass

  def printList(self):
    cur = self.head
    while cur:
      print(cur.value)
      cur = cur.next

d = DoublyLinkedList()
d.add_to_head(3)
d.add_to_head(2)
d.add_to_head(1)
d.add_to_head(0)
d.add_to_tail(4)
d.add_to_tail(5)
d.remove_from_head()
d.remove_from_tail()
d.printList()