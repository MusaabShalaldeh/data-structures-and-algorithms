# Trees

A tree data structure in which each node has at most two children, which are referred to as the left child and the right child. A recursive definition using just set theory notions is that a (non-empty) binary tree is a tuple (L, S, R), where L and R are binary trees or the empty set and S is a singleton set containing the root.

## Challenge
Creating a binary tree class with its methods

## Approach & Efficiency


Approach: TDD

Efficiency:
-Time O(log n)
-Space O(log h)

## API


    bfs(self)
    """
    A binary tree method which returns a list of items that it contains

    input: None

    output: tree items
    """

    pre_order(self)
    """
    A binary tree method which returns a list of items that it contains

    input: None

    output: tree items

    sub method : walk () to make the recursion staff
    """


    in_order(self)
    """
    function to in order the list using Trees
    """

    post_order(self)
    """
    A binary tree method which returns a list of items in post order

    input: None

    output: tree items
    """
