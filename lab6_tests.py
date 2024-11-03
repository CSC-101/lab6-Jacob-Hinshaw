import data
import lab6
import unittest

from lab6 import selection_sort, selection_sort_alpha


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test1_selection_sort_alpha(self):
        input1 = [data.Book(["Jacob"], "Unicycle"), data.Book(["Sophia"], "Flute"),
                  data.Book(["Travis"], "Soccer")]
        expected = [data.Book(["Sophia"], "Flute"), data.Book(["Travis"], "Soccer"),
                    data.Book(["Jacob"], "Unicycle")]
        lab6.selection_sort_alpha(input1)
        self.assertEqual(expected, input1)
    def test2_selection_sort_alpha(self):
        input1 = [data.Book(["Jacob"], "aabb"), data.Book(["Sophia"], "aaab"),
                  data.Book(["Travis"], "abbb")]
        expected = [data.Book(["Sophia"], "aaab"), data.Book(["Jacob"], "aabb"),
                    data.Book(["Travis"], "abbb")]
        lab6.selection_sort_alpha(input1)
        self.assertEqual(expected, input1)

    # Part 2
    def test1_swap_case(self):
        input1 = "Hey There!"
        result = lab6.swap_case(input1)
        expected = "hEY tHERE!"
        self.assertEqual(expected, result)
    def test2_swap_case(self):
        input1 = "abcABC123"
        result = lab6.swap_case(input1)
        expected = "ABCabc123"
        self.assertEqual(expected, result)

    # Part 3
    def test1_str_translate(self):
        input1 = "Hey There!"
        result = lab6.str_translate(input1, "e", "a")
        expected = "Hay Thara!"
        self.assertEqual(expected, result)
    def test2_str_translate(self):
        input1 = "123321"
        result = lab6.str_translate(input1, "2", "6")
        expected = "163361"
        self.assertEqual(expected, result)

    # Part 4
    def test1_histogram(self):
        input1 = ("Hey there!")
        result = lab6.histogram(input1)
        expected = {"Hey":1, "there!":1}
        self.assertEqual(expected, result)
    def test2_histogram(self):
        input1 = ("ooo aaa ooo aaa ooo ooo")
        result = lab6.histogram(input1)
        expected = {"ooo":4, "aaa":2}
        self.assertEqual(expected, result)




if __name__ == '__main__':
    unittest.main()
