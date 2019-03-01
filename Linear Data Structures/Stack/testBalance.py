# Author: Adi Laiman
# Date: 01 March 2019 (01-03-2019)
# Email: laiman@posteo.de

# unit test to check balancedParentheses.py
from balancedParentheses import *
from colorama import *

def balanced_1():
    assert balanced("(()()()())") == True

def balanced_2():
    assert balanced("(((())))") == True

def balanced_3():
    assert balanced("(()((())()))") == True

def unbalanced_1():
    assert balanced("((((((())") == False

def unbalanced_2():
    assert balanced("()))") == False

def unbalanced_3():
    assert balanced("(()()(()") == False

if __name__ == "__main__":
    try:
        init()
        balanced_1()
        balanced_2()
        balanced_3()
        unbalanced_1()
        unbalanced_2()
        unbalanced_3()
        print(Fore.GREEN + "All tests passed." + Style.RESET_ALL)
        deinit()
    except AssertionError:
        print(Fore.RED + "Test failed." + Style.RESET_ALL)
        deinit()