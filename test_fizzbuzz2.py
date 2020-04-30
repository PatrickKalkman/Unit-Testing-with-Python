import unittest

class FizzBuzzTest(unittest.TestCase):

    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def tearDown(self):
        pass

    def test_one_should_return_one(self):
        result = self.fizzbuzz.filter(1)
        self.assertEqual('1', result)

    def test_two_should_return_two(self):
        result = self.fizzbuzz.filter(2)
        self.assertEqual('2', result)


class FizzBuzz:
	
    def filter(self, number):
        return str(number)