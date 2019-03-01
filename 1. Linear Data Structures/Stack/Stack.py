class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

    # can also implement a stack where items are pushed to the bottom
    #  def push(self, item):
    #      self.items.insert(0,item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[-1]

     def size(self):
         return len(self.items)

if __name__ == "__main__":
    newStack = Stack()
    print(newStack.isEmpty())
    newStack.push(8)
    newStack.push("foobar")
    print(newStack.peek())
    newStack.push(True)
    print(newStack.size())
    print(newStack.pop())
    print(newStack.pop())