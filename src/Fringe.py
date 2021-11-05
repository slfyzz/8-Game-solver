from abc import ABC, abstractmethod
from queue import PriorityQueue as PriorityLinkedList, Queue as LinkedList
from src.state import State


class Fringe(ABC):

    def __init__(self):
        self.queue = []

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def push(self, state: State):
        pass

    @abstractmethod
    def isEmpty(self):
        return len(self.queue) == 0


class Stack(Fringe, ABC):

    def __init__(self):
        super().__init__()

    def pop(self):
        return self.queue.pop()

    def push(self, state: State):
        return self.queue.append(state)


class Queue(Fringe, ABC):

    def __init__(self):
        super().__init__()
        self.queue = LinkedList()

    def pop(self):
        return self.queue.get()

    def push(self, state: State):
        return self.queue.put(state)

    def isEmpty(self):
        return self.queue.empty()


class PriorityQueue(Fringe, ABC):

    def __init__(self, priorityCalculator):
        super().__init__()
        self.queue = PriorityLinkedList()
        self.priorityCalculator = priorityCalculator

    def pop(self):
        return self.queue.get()[1]

    def push(self, state: State):
        return self.queue.put((self.priorityCalculator.calc(state), state))

    def isEmpty(self):
        return self.queue.empty()
