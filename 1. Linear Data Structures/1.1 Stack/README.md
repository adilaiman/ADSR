## 1.1 Stacks
A stack is an ordered collection such that items are added and removed from the "same end", this end is commonly referred to as the "top", the opposite end is referred as the "base". This ordering principle is called **LIFO**, **last-in first-out**. Newer items are at the top and removed first, older items are at the base and removed last.

### 1.1.2 Python 3 Stack Commands
```python
Stack() #creates a new stack that is empty. It needs no parameters and returns an empty stack.
push(item) #adds a new item to the top of the stack. It needs the item and returns nothing.
pop() #removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
peek() #returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
isEmpty() #tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
size() #returns the number of items on the stack. It needs no parameters and returns an integer.
```

### 1.1.3 Using Stacks
The challenge then is to write an algorithm that will read a string of parentheses from left to right and decide whether the symbols are balanced.

#### 1.1.4 Examples of balanced and unbalanced.
```
Balanced

(()()()())

(((())))

(()((())()))
```

```
Unbalanced

((((((())

()))

(()()(()
```

#### 1.1.5 Solution
Starting with an empty stack, process the parenthesis strings from left to right. If a symbol is an opening parenthesis, push it on the stack as a signal that a corresponding closing symbol needs to appear later. If, on the other hand, a symbol is a closing parenthesis, pop the stack. As long as it is possible to pop the stack to match every closing symbol, the parentheses remain balanced. If at any time there is no opening symbol on the stack to match a closing symbol, the string is not balanced properly. At the end of the string, when all symbols have been processed, the stack should be empty.

Test your own solutions by making sure your python file is name **balancedParentheses.py** and then running the **testBalance.py** file.

```python
python testBalance.py
```