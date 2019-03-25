# Author: Adi Laiman
# Date: 25 March 2019 (25-03-2019)
# Email: laiman@posteo.de

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

if __name__=="__main__":
    q=Queue()
	
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())