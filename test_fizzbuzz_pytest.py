import pytest
from fizzbuzz import FizzBuzz 

@pytest.fixture
def fizzBuzz():
    return FizzBuzz()

def test_one_should_return_one(fizzBuzz):
    result = fizzBuzz.filter(1)
    assert result == '1'

def test_two_should_return_two(fizzBuzz):
    result = fizzBuzz.filter(2)
    assert result == '2'

def test_three_should_return_fizz(fizzBuzz):
    result = fizzBuzz.filter(3)
    assert result == 'Fizz'

def test_five_should_return_buzz(fizzBuzz):
    result = fizzBuzz.filter(5)
    assert result == 'Buzz'

def test_fifteen_should_return_fizzbuzz(fizzBuzz):
    result = fizzBuzz.filter(15)
    assert result == 'FizzBuzz'