class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
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



class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self,animal: str):
        if animal.lower() == "cat":
            self.cats.enqueue("cat")
        elif animal.lower() == "dog":
            self.dogs.enqueue("cat")
        else:
            raise WrongShelterInput("Wrong Input, has to be either cat or dog!")

    def dequeue(self,pref: str):
        if not pref.lower()=="cat" and not pref.lower()== "dog":
            return None
        elif self.dogs.is_empty() and self.cats.is_empty():
            raise EmptyQueue("Animal Shelter Queue is empty, can't remove or return a value!")
        elif pref.lower() == "cat" and not self.cats.is_empty():
            return self.cats.dequeue()
        elif pref.lower() == "dog" and not self.dogs.is_empty():
            return self.dogs.dequeue()
        elif pref.lower() == "cat" and self.cats.is_empty() and not self.dogs.is_empty():
            return self.dogs.dequeue()
        elif pref.lower() == "dog" and self.dogs.is_empty() and not self.cats.is_empty():
            return self.cats.dequeue()
        else:
            return None


class EmptyQueue(Exception):
    pass

class WrongShelterInput(Exception):
    pass
