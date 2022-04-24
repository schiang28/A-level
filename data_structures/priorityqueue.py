class QueueItem:
  def __init__(self, item, priority):
    self.item = item
    self.priority = priority
    # for whoever is behind me 
    self._next = None

  def setNext(self, q):
    self._next = q

  def getNext(self):
    return self._next

class Queue:
  def __init__(self):
    self._head = None
    self._tail = None

  def isEmpty(self):
    return self._head == None

  def enqueue(self, item, priority):
    qNext = QueueItem(item, priority)
    if self.isEmpty():
      self._head = qNext
      self._tail = qNext
    else:
      pointer = self._head
      prev = None
      while not pointer == None and priority >= pointer.priority:
        prev = pointer
        pointer = pointer.getNext()
      if prev != None:
        prev.setNext(qNext)
      else:
        self._head = qNext
      qNext.setNext(pointer)
      if pointer == None:
        self._tail = qNext

  def dequeue(self):
    if self.isEmpty():
      print("error, very bad, go away")
      return
    else:
      q = self._head
      self._head = q.getNext()
      return q.item

printJobs = Queue()
printJobs.enqueue("Mr Baker's print job", 10)
printJobs.enqueue("Mr Ingram's print job", 1)
printJobs.enqueue("Mrs Hague's print job", 5)
printJobs.enqueue("Mr Gwilt's print job", 10)

while not printJobs.isEmpty():
  print(printJobs.dequeue())