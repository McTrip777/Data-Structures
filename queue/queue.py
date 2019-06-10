class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.storage.insert(0, item)
  
  def dequeue(self):
    self.storage.pop()

  def len(self):
    return len(self.storage)
 
  def printQueue(self):
    # for item in self.storage:
      print(self.storage)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.len()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.dequeue()
q.printQueue()

