class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.q = []
        self.maxsize = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        self.q.append(value)
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.q.pop(0)
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if len(self.q) == 0:
            return -1
        else:
            return self.q[0]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.q[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return len(self.q) <= 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return len(self.q) == self.maxsize

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

k = MyCircularQueue(3)
print(k.enQueue(2))
print(k.enQueue(5))
print(k.enQueue(10))
print(k.enQueue(1))
print(k.Front())
print(k.Rear())
print(k.deQueue())
print(k.enQueue(1))
print(k.Front())
print(k.Rear())