from stack_and_queue.node import Node
from stack_and_queue.stack import Stack


class Queue:
    """
    Class: Queue

    """

    def __init__(self):
        self.front = None
        self.rear = None


    def enqueue(self,value):
        node = Node(value)
        if self.front == None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front == None:
            raise EmptyQueue("Empty Queue! can't dequeue an empty queue.")
        elif self.front.next == None:
            temp_node = self.front
            self.front = None

            return temp_node.value
        else:
            temp_node = self.front
            self.front = self.front.next

            return temp_node.value

    def peek(self):
        if self.front != None:
            return self.front.value
        else:
            raise EmptyQueue("Empty Queue! can't return the front of the queue")

    def is_empty(self):
        return not self.front


class PsuedoQueue:
    def __init__(self):
        self.first_stack = Stack()
        self.second_stack = Stack()

    def enqueue(self,value):
        self.first_stack.push(value)

    def dequeue(self):
        if self.first_stack.is_empty() and self.second_stack.is_empty():
            raise EmptyQueue("Error: dequeueing on an empty queue.")
        if self.second_stack.is_empty():
            while not self.first_stack.is_empty():
                temporary_item = self.first_stack.pop()
                self.second_stack.push(temporary_item)
        return self.second_stack.pop()


class EmptyQueue(Exception):
    pass
