import unittest
from sort_and_search import insertion_sort, binary_search, linear_search

class TestExamples(unittest.TestCase):

    def test_insertion_sort(self):
        #Arrange:
        num_array = [5, 2, 1, 8, 9, 3]
        #Act:
        result = insertion_sort(num_array)
        #Assert:
        self.assertEqual(result, [1, 2, 3, 5, 8, 9])

    def test_binary_search_found(self):
        #Arrange:
        num_array = [1, 2, 3, 4, 5, 6]
        target = 5
        #Act:
        result = binary_search(num_array, target)
        #Assert:
        self.assertEqual(result, 4)

    def test_binary_search_not_found(self):
        #Arrange:
        num_array = [1, 2, 3, 4, 5, 6]
        target = 7
        #Act:
        result = binary_search(num_array, target)
        #Assert:
        self.assertEqual(result, -1)

    def test_linear_search_found(self):
        #Arrange:
        num_array = [1, 2, 3, 4, 5, 6]
        target = 5
        #Act:
        result = linear_search(num_array, target)
        #Assert:
        self.assertEqual(result, 4)

    def test_linear_search_not_found(self):
        #Arrange:
        num_array = [1, 2, 3, 4, 5, 6]
        target = 7
        #Act:
        result = linear_search(num_array, target)
        #Assert:
        self.assertEqual(result, -1)

    def test_one_linear_search(self):
        #Arrange:
        num_array = [4]
        target = 4
        #Act:
        result = linear_search(num_array, target)
        #Assert:
        self.assertEqual(result, 0)

    def test_one_binary_search(self):
        #Arrange:
        num_array = [4]
        target = 4
        #Act:
        result = linear_search(num_array, target)
        #Assert:
        self.assertEqual(result, 0)

    def test_lots_of_elements_linear_search(self):
        #Arrange: 
        #makes a list from 0 to 2147483646 which is maximum for 32 bit       
        arr = list(range(2**31 - 1))
        target = 999999
        #Act
        result = linear_search(arr, target)
        #Assert:
        self.assertEqual(result, 999999)
        #Took 296.278s

    def test_lots_of_elements_binary_search(self):
        #Arrange: 
        #makes a list from 0 to 2147483646 which is maximum for 32 bit       
        arr = list(range(2**31 - 1))
        target = 999999
        #Act
        result = binary_search(arr, target)
        #Assert:
        self.assertEqual(result, 999999)
        #Took 283.032s






if __name__ == '__main__':
    unittest.main()