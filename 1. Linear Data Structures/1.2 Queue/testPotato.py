
# Author: Adi Laiman
# Date: 25 March 2019 (25-03-2019)
# Email: laiman@posteo.de

# unit test to check hotPotato.py
from hotPotato import *
from colorama import *

def susan():
    assert hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7) == "Susan"

def jane():
    assert hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],10) == "Jane"

def bill():
    assert hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],20) == "Bill"

def kent():
    assert hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],6) == "Kent"

if __name__=="__main__":
    try:
        init()
        susan()
        jane()
        bill()
        kent()
        print(Fore.GREEN + "All test passed." + Style.RESET_ALL)
        deinit()
    except AssertionError:
        print(Fore.RED + "Test failed." + Style.RESET_ALL)
        deinit()