'''
https://www.testdome.com/questions/python/train-composition/40609

A TrainComposition is built by attaching and detaching wagons from the left and the right sides, efficiently with respect to time used.

For example, if we start by attaching wagon 7 from the left followed by attaching wagon 13, again from the left, we get a composition of two wagons (13 and 7 from left to right). Now the first wagon that can be detached from the right is 7 and the first that can be detached from the left is 13.

Implement a TrainComposition that models this problem.
'''
from collections import deque

class TrainComposition:

    def __init__(self):
        self.d = deque()
    
    def attach_wagon_from_left(self, wagonId):
        self.d.appendleft(wagonId)
    
    def attach_wagon_from_right(self, wagonId):
        self.d.append(wagonId)

    def detach_wagon_from_left(self):
        return self.d.popleft()
    
    def detach_wagon_from_right(self):
        return self.d.pop()

train = TrainComposition()
train.attach_wagon_from_left(7)
train.attach_wagon_from_left(13)
print(train.detach_wagon_from_right()) # should print 7
print(train.detach_wagon_from_left()) # should print 13
