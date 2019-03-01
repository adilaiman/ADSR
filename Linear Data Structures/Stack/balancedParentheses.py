# Author: Adi Laiman
# Date: 01 March 2019 (01-03-2019)
# Email: laiman@posteo.de

from Stack import *

def balanced(stringOfP):
    pStack = Stack()
    i = 0
    balanced = True

    while i < len(stringOfP) and balanced == True:
        currentChar = stringOfP[i]
        if currentChar == "(":          # If opening bracket then we push to stack
            pStack.push(currentChar)
        elif not pStack.isEmpty():      # Else if it is closing bracket, we pop if stack is not empty
            pStack.pop()
        else:                           # If there are no matching pairs to pop then it is unbalanced
            balanced = False
        i+=1

    return (balanced and pStack.isEmpty())

if __name__ == "__main__":
    print(balanced('((()))')) # True
    print(balanced('(()')) # False