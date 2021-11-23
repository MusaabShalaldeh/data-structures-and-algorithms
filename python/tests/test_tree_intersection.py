from code_challenges.tree_intersection.tree_intersection import tree_intersection
import pytest
from data_strtucture.trees.trees import BinaryTree, Node


@pytest.fixture
def tree_one():
    tree = BinaryTree()
    a_node = Node(100,left=Node(6),right=Node(17))
    a_node.right.left = Node(15)
    a_node.right.right = Node(1)
    tree.root = a_node
    return tree

@pytest.fixture
def tree_two():
    tree = BinaryTree()
    a_node = Node(10,left=Node(6),right=Node(13))
    a_node.right.left = Node(15)
    a_node.right.right = Node(93)
    tree.root = a_node
    return tree

@pytest.fixture
def short_tree():
    tree = BinaryTree()
    a_node = Node(10,left=Node(6),right=Node(13))
    tree.root = a_node
    return tree

@pytest.fixture
def empty_tree():
    tree = BinaryTree()
    return tree

@pytest.fixture
def empty_tree_two():
    tree = BinaryTree()
    return tree

def test_tree_intersection(tree_one, tree_two):
    # Arrange
    expected = ["6","15"]
    # Actual
    actual = tree_intersection(tree_one,tree_two)
    # Expected
    assert actual == expected

def test_tree_intersection_two(tree_one, short_tree):
    # Arrange
    expected = ["6"]
    # Actual
    actual = tree_intersection(tree_one, short_tree)
    # Expected
    assert actual == expected

def test_tree_intersection_short_tree_and_longer_tree(tree_one, short_tree):
    # Arrange
    expected = ["6"]
    # Actual
    actual = tree_intersection(short_tree, tree_one)
    # Expected
    assert actual == expected


def test_tree_intersection_empty_tree(tree_one, empty_tree):
    # Arrange
    expected = []
    # Actual
    actual = tree_intersection(tree_one, empty_tree)
    # Expected
    assert actual == expected


def test_tree_intersection_two_empty_tree(empty_tree, empty_tree_two):
    # Arrange
    expected = []
    # Actual
    actual = tree_intersection(empty_tree, empty_tree_two)
    # Expected
    assert actual == expected



