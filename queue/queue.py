class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    return self.storage.insert(0, item)
  
  def dequeue(self):
    if len(self.storage):
      return self.storage.pop()

  def len(self):
    return len(self.storage)
 

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.dequeue()
