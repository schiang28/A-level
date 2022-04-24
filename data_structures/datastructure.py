'''class Stack:
    def __init__(self, size=0):
        self.contents = [None for _ in range(size)]
        self.max = size
        self.pointer = -1

    def isFull(self):
        if self.pointer == self.max - 1:
            return True
        return False

    def push(self, item):
        if self.isFull():
            raise IndexError("Stack full error")

        self.pointer += 1
        self.contents[self.pointer] = item
        print("pushed", item)

    def isEmpty(self):
        if self.pointer == -1:
            return True
        return False

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack empty error")

        item = self.contents[self.pointer]
        self.pointer -= 1
        print("popped", item)
        return item

    def peek(self):
        if self.isEmpty():
            raise IndexError("Stack empty error")

        item = self.contents[self.pointer]
        print("peeked", item)
        return item
'''

class Array:
    def __init__(self, type, size = 0):
        self.contents = [type() for _ in range(size)]
        self.type = type
        self.maxSize = size
    
    def __getitem__(self, index):
        if 0 <= index <= self.maxSize:
            return self.contents[index]
        else:
            raise IndexError("Array index out of range")

    def __setitem__(self, index, item):
        if type(item) != self.type:
            raise ValueError(f"Cannot write {type(item)} object to array of type: {self.type}")
        if 0 <= index <= self.maxSize:
            self.contents[index] = item
        else:
            raise IndexError("Array index out of range")
    
    def __str__(self):
        return "Array contains: " + " ".join([str(i) for i in self.contents])


class StackItem:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self):
        self._head = None

    def isEmpty(self):
        return self._head == None

    def isFull(self):
        # dynamic so never full
        return False

    def push(self, item):
        stackItem = StackItem(item)
        # create stackItem object
        if not self.isEmpty():
            stackItem.next = self._head
        # if the stack is not empty
        self._head = stackItem
        # set the current head to the new stackItem's next attribute
        # set the head to the new stackItem

    def pop(self):
        if not self.isEmpty():
            stackItem = self._head
            self._head = self._head.next
            return stackItem.item
        else:
            raise ValueError("nothing left to pop")

    def peek(self):
        if not self.isEmpty():
            return self._head.item
        else:
            raise ValueError("Nothing to peek")
 

'''
if __name__ == "__main__":

    a = Stack()

    a.push("1")
    a.push("2")
    a.push("4")
    a.push("28")
    a.push("30")

    a.peek()

    a.pop()
'''

# a = Stack(5)

# a.push("This")
# a.push("is")
# a.push("a")
# a.push("test")
# a.push("ha")

# for _ in range(5):
#     a.pop()

'''
# array

b = Array(int, 10)
for i in range(10):
    b[i] = i

print(b[3])
'''