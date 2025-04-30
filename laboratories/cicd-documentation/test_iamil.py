from tree import Tree
from node import Node

tree = Tree()

tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
tree._printInorderTree(tree.root)
tree._printPostorderTree(tree.root)
tree._printPreorderTree(tree.root)


def test_find():
    tree = Tree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)
    assert tree.find(3).data == 3
    assert tree.find(4).data == 4
    assert tree.find(0).data == 0
    assert tree.find(8).data == 8
    assert tree.find(2).data == 2
    assert tree.find(5) is None

def test_find_advanced():
    tree = Tree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)
    assert tree.find(3).data == 3
    assert tree.find(4).data == 4
    assert tree.find(0).data == 0
    assert tree.find(8).data == 8
    assert tree.find(2).data == 2

    tree.deleteTree()
    assert tree.find(3) is None

    tree = Tree()
    tree.add(69)
    assert tree.getRoot().data == 69
    assert tree.find(69).data == 69
    assert tree.find(0) is None