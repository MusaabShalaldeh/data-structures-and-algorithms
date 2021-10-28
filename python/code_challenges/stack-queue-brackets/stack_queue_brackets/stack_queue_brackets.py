class Node:
    """
    Class: Code
    A class that respresnts an object which contains its own value and a pointer to the next object in line.

    Arguments: Value
    returns: None
    """
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

class Stack:
    """
    Class: Stack

    """
    def __init__(self):
        self.top = None

    def push(self,value):
        if self.top == None:
            self.top = Node(value)
        else:
            self.top = Node(value,self.top)

    def pop(self):
        if(self.top != None):
            last_top = self.top.value
            if self.top.next != None:
                self.top = self.top.next
                return last_top
            else:
                self.top = None
                return last_top
        else:
            raise EmptyStack("Errour encounted....Stack is empty.")

    def peek(self):
        return self.top.value

    def is_empty(self):
        if self.top == None:
            return True
        return False

class EmptyStack(Exception):
    pass



def ValidateBrackets(string: str):
    if type(string) is not str:
        return None

    opening_brackets = ["{","[","("]
    closing_brackets = ["}","]",")"]
    matches = Stack()

    for i in string:
        if i in opening_brackets:
            matches.push(i)
        elif i in closing_brackets:
            if not matches.is_empty() and ("{" == matches.peek() or "(" == matches.peek() or "[" == matches.peek()):
                matches.pop()
            else:
                return False
    # if matches stack is empty, it means that there are not any unbalanced brackets
    if matches.is_empty():
        return True
    else:
        return False


if __name__ == "__main__":
    ValidateBrackets("[](})")
