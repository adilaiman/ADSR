# Author: Adi Laiman
# Date: 25 March 2019 (25-03-2019)
# Email: laiman@posteo.de

from Queue import *

# namelist is the participants
# num is the amount of times to pass the potato
def hotPotato(namelist, num):

    # create queue and add everyone to it
    circleOfPeople = Queue()
    for name in namelist:
        circleOfPeople.enqueue(name)

    while circleOfPeople.size() > 1:
        for i in range(num):
            # move people in front to end of the queue
            circleOfPeople.enqueue(circleOfPeople.dequeue())
        # at the end of time remove the person in front (person holding potato)
        circleOfPeople.dequeue()

    # return the last person remaining
    return circleOfPeople.dequeue()