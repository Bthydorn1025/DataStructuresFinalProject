import unittest
from DataStructuresFinalProject import Queue
from DataStructuresFinalProject import Node

"""class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)"""

class testSizeCase(unittest.TestCase):
    def test_size(self):
        #Arrange
        q = Queue()
        q.enqueue(5)
        q.enqueue(3) #queueing elements to make size of 5
        q.enqueue(2)
        q.enqueue(6)
        q.enqueue(1)
        #Act
        expected = 5 #expected is a size of 5
        actual = q.size() #actual is the returned output of the size algorithm.
        #Assert
        self.assertEqual(expected, actual)

class testIsEmptyFunction(unittest.TestCase):
    def test_isEmptyTrue(self):
        #Arrange
        q = Queue()
        #Act
        expected = True
        actual = q.isEmpty()
        #Assert
        self.assertEqual(expected, actual)

    def test_isEmptyFalse(self):
        #Arrange
        q = Queue()
        q.enqueue(12)
        #Act
        expected = False
        actual = q.isEmpty()
        #Assert
        self.assertEqual(expected, actual)

class testPrintFunction(unittest.TestCase):
    def test_printsolution(self):
        #Arrange
        q = Queue()
        q.enqueue(1.5)
        q.enqueue(3.1)
        q.enqueue(4.0)

        #Act
        expected = print(" 1.5 3.1 4.0 ")
        actual = q.printSolution()
        #Assert
        self.assertEqual(expected, actual)

class testSortingFunction(unittest.TestCase):
    def test_BubbleSort(self):
        #Arrange
        q = Queue()
        q.enqueue(2.5)
        q.enqueue(1.4)
        q.enqueue(3.5)
        q.enqueue(2.1)
        q.enqueue(3.0)
        #Act
        expected = print(" 1.4 2.1 2.5 3.0 3.5 ")
        q.bubbleSort()
        actual = q.printSolution()
        #Assert
        self.assertEqual(expected, actual)

class testDequeueFunction(unittest.TestCase):
    def test_Dequeue(self):
        #Arrange
        q = Queue()
        q.enqueue(1.1)
        q.enqueue(2.2)
        q.enqueue(3.3)
        q.enqueue(4.4)
        q.dequeue()
        #Act
        expected = print(" 2.2 3.3 4.4 ")
        actual = q.printSolution()
        #Assert
        self.assertEqual(expected, actual)
if __name__ == '__main__':
    unittest.main()
