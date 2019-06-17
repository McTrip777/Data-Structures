class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
      if value < self.value:
          if not self.left:
              self.left = BinarySearchTree(value)
          else:
              self.left.insert(value)
      elif value >= self.value:
          if self.right is None:
              self.right = BinarySearchTree(value)
          else:
              self.right.insert(value)

  def contains(self, target):
        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        else:
            return True

  def get_max(self):
    current = self
    while current.right:
      current = current.right
    return current.value

  def for_each(self, cb):
    cb(self.value)
    if self.right:
        self.right.for_each(cb)
    if self.left:
        self.left.for_each(cb)
    



root = BinarySearchTree(50)
root.insert(5)
root.insert(68)
root.insert(72)
root.insert(20)
root.insert(29)
root.contains(49)
root.get_max()
