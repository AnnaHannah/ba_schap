from RedBlackTree import RedBlackTree
import unittest
from random import seed, randint
from timeit import Timer

class RedBlackTreeTest(unittest.TestCase):

    def setUp(self):
        seed(0)
        self.sl = RedBlackTree()

    # Test insert(elem)
 
    def testInsertionInEmptyTree(self):
        self.sl.insert(1)
        self.assertTrue(self.sl.searchTree(1))
        self.assertFalse(self.sl.searchTree(2))

    def testInsersionAtTheBeginningOfTheTree(self):
        self.sl.insert(2)
        self.sl.insert(1)
        self.assertTrue(self.sl.searchTree(1))
        self.assertTrue(self.sl.searchTree(2))
        
    def testInsersionAtTheEndOfTheTree(self):
        self.sl.insert(1)
        self.sl.insert(2)
        self.assertTrue(self.sl.searchTree(1))
        self.assertTrue(self.sl.searchTree(2))

    def testInsertionOfTheSameElement(self):
        self.sl.insert(1)
        self.sl.insert(1)
        self.assertTrue(self.sl.searchTree(1))
        self.assertEqual(1, len(self.sl))

    # Test remove(elem)

    def testRemovalFromASingleElementTree(self):
        self.sl.insert(1)
        self.assertTrue(self.sl.delete_node(1))
        self.sl.delete_node(1)
        self.assertFalse(self.sl.delete_node(1))

    def testRemovalFromAnElementNotInTheTree(self):
        self.sl.delete_node(1)
        self.sl.insert(1)
        self.assertTrue(self.sl.delete_node(1))
        self.sl.delete_node(2)
        self.assertTrue(self.sl.delete_node(1))

    # Test find(elem)

    def testFindingOfASingleElementTree(self):
        self.sl.insert(1)
        node = self.sl.searchTree(1)
        self.assertEqual(1, node.elem)

    def testFindingOfTheMiddleElementTree(self):
        self.sl.insert(1)
        self.sl.insert(2)
        self.sl.insert(3)
        node = self.sl.searchTree(2)
        self.assertEqual(2, node.elem)

    def testFindingAnElementNotInTheTree(self):
        self.assertEqual(None, self.sl.searchTree(1))
 
if __name__ == '__main__':
    unittest.main()