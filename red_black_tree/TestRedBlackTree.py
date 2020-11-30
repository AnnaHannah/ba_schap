from RedBlackTree import RedBlackTree
import unittest
from random import seed, randint
from timeit import Timer

class RedBlackTreeTest(unittest.TestCase):

    def setUp(self):
        seed(0)
        self.rb = RedBlackTree()

    # Test insert(elem)
 
    def testInsertionInEmptyTree(self):
        self.rb.insert(1)
        self.assertTrue(self.rb.searchTree(1))
        self.assertFalse(self.rb.searchTree(2))

    def testInsersionAtTheBeginningOfTheTree(self):
        self.rb.insert(2)
        self.rb.insert(1)
        self.assertTrue(self.rb.searchTree(1))
        self.assertTrue(self.rb.searchTree(2))
        
    def testInsersionAtTheEndOfTheTree(self):
        self.rb.insert(1)
        self.rb.insert(2)
        self.assertTrue(self.rb.searchTree(1))
        self.assertTrue(self.rb.searchTree(2))

    def testInsertionOfTheSameElement(self):
        self.rb.insert(1)
        self.rb.insert(1)
        # self.assertTrue(self.rb.searchTree(1))
        # self.assertEqual(1, len(self.rb))

    # Test remove(elem)

    def testRemovalFromASingleElementTree(self):
        self.rb.insert(1)
        self.assertTrue(self.rb.delete_node(1))
        self.rb.delete_node(1)
        self.assertFalse(self.rb.delete_node(1))

    def testRemovalFromAnElementNotInTheTree(self):
        self.rb.delete_node(1)
        self.rb.insert(1)
        self.assertTrue(self.rb.delete_node(1))
        self.rb.delete_node(2)
        self.assertTrue(self.rb.delete_node(1))

    # Test find(elem)

    def testFindingOfASingleElementTree(self):
        self.rb.insert(1)
        node = self.rb.searchTree(1)
        self.assertEqual(1, node.data)

    def testFindingOfTheMiddleElementTree(self):
        self.rb.insert(1)
        self.rb.insert(2)
        self.rb.insert(3)
        node = self.rb.searchTree(2)
        self.assertEqual(2, node.data)

    def testFindingAnElementNotInTheTree(self):
        self.assertEqual(None, self.rb.searchTree(1))
 
if __name__ == '__main__':
    unittest.main()