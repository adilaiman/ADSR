## 1.2 Queue
The queue like a queue in real life is a data structure in which new items "queue" or get added to the end. This ordering principle is sometimes called **FIFO**, first-in first-out.

### 1.1.2 Python 3 Queue Commands
```python
Queue() #creates a new queue that is empty. It needs no parameters and returns an empty queue.
enqueue(item) #adds a new item to the rear of the queue. It needs the item and returns nothing.
dequeue() #removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
isEmpty() #tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
size() #returns the number of items in the queue. It needs no parameters and returns an integer.
```

### 1.1.3 Using Queues

The exercise is to write a simulation for hot potato. Hot potato is a game in which a group of people pass a potato for a certain amount of time and whomever is holding said potato is eliminated. 

### 1.1.5 Solution

The way to approach this problem is to have a circular queue in which the people in the front are moved to the back. This happens for *x* times before stopping, when stopped that person is eliminated and so is removed from the queue. We keep doing this until there is only 1 person in the queue.

Check the solution **hotPotato.py** in this folder if you are stuck.

Test your own solutions by making sure your python file is named **hotPotato.py** and then running the **testPotato.py** file.

```python
python testPotato.py
```