"""
This Module defines a Node and a Binary Tree
"""

class Node:
  def __init__ (self,data,left=None,right=None):
    self.data = data
    self.left = left
    self.right = right

class Queue:
  def __init__(self, collection=[]):
    self.data = collection

  def peek(self):
    if len(self.data):
      return True
    return False

  def enqueue(self,item):
    self.data.append(item)

  def dequeue(self):
    return self.data.pop(0)

class BinaryTree:

    def __init__(self):
        self.root = None

    def bfs(self):
        """
        A binary tree method which returns a list of items that it contains

        input: None

        output: tree items
        """
        # Queue breadth <-- new Queue()
        breadth = Queue()
        # breadth.enqueue(root)
        breadth.enqueue(self.root)

        list_of_items = []

        while breadth.peek():
            front = breadth.dequeue()
            list_of_items += [front.data]

            if front.left:
                breadth.enqueue(front.left)

            if front.right:
                breadth.enqueue(front.right)

        return list_of_items

    def pre_order(self):
        """
        A binary tree method which returns a list of items that it contains

        input: None

        output: tree items

        sub method : walk () to make the recursion staff
        """
        list_of_items = []
        def walk(node):
            if node:
                list_of_items.append(node.data)
                if node.left:
                    walk(node.left)
                if node.right:
                    walk(node.right)

        walk(self.root)
        return list_of_items

    def in_order(self):
        """
        function to in order the list using Trees
        """
        list_of_items = []
        def walk(node):
            if node:
                if node.left:
                    walk(node.left)
                list_of_items.append(node.data)
                if node.right:
                    walk(node.right)

        walk(self.root)
        return list_of_items

    def post_order(self):
        """
        A binary tree method which returns a list of items in post order

        input: None

        output: tree items
        """
        list_of_items = []
        def walk(node):
            if node:
                if node.left:
                    walk(node.left)
                if node.right:
                    walk(node.right)

            list_of_items.append(node.data)

        walk(self.root)
        return list_of_items


class BinarySearchTree(BinaryTree):
    """
    Binary Tree Class

    A class that extends BiaryTree class with 2 new methods:

    Method: Add
        Args:
        value

    Returns:
        None

    Method: Contains
        Args:
            Value

        Returns:
            True or False
    """

    def add(self,data):
        if not self.root:
            self.root= Node(data)
        else:
            if self.root.data < data:
                if not self.root.right:
                    self.root.right = Node(data)
                else:
                    self.add(data)
            else:
                if not self.root.left:
                    self.root.left = Node(data)
                else:
                    self.add(data)

    def contains(self,value):
        items = self.bfs()

        for item in items:
            if item == value:
                return True
        return False




def compare_tree_files_num(directory_one: BinaryTree, directory_two: BinaryTree):

    queue = Queue()
    counter_one = 0
    counter_two = 0

    def get_files_num(root):
        queue.enqueue(root)
        counter = 0
        while queue.peek():
            front = queue.dequeue()
            if not front.left and not front.right:
                counter +=1

            if front.left:
                queue.enqueue(front.left)
            if front.right:
                queue.enqueue(front.right)
        return counter

    counter_one = get_files_num(directory_one.root)
    counter_two = get_files_num(directory_two.root)


    return True if counter_one == counter_two else False



if __name__ == "__main__":
    first_tree = BinaryTree()
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    first_tree.root = a_node

    second_tree = BinaryTree()
    a_node = Node('1')
    a_node.left = Node('2')
    b_node = Node('3')
    b_node.left = Node("15")
    b_node.right = Node("3")
    a_node.right = b_node

    second_tree.root = a_node


    print(compare_tree_files_num(first_tree,second_tree))
