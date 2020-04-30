import unittest
from fizzbuzz import FizzBuzz 

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

    def test_three_should_return_fizz(self):
        result = self.fizzbuzz.filter(3)
        assert result == 'Fizz'

    def test_five_should_return_buzz(self):
        result = self.fizzbuzz.filter(5)
        assert result == 'Buzz'

    def test_fifteen_should_return_fizzbuzz(self):
        result = self.fizzbuzz.filter(15)
        assert result == 'FizzBuzz'