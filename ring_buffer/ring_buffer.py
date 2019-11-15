class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current < self.capacity:
      print('current less than capacity, see', self.current, self.capacity)
      self.storage.pop(0)
      self.storage.append(item)
      self.current +=1
    else:
      print('now reached capacity')
      self.storage[self.current%self.capacity] = item
      print(self.storage)
      self.current +=1
  def get(self):
    return [i for i in self.storage if i is not None]


buffer = RingBuffer(5)
buffer_2 = RingBuffer(5)

buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
buffer.append('f')
print(buffer.get())