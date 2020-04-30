import pytest

@pytest.fixture
def fizzBuzz():
    return FizzBuzz()

def test_one_should_return_one(fizzBuzz):
    result = fizzBuzz.filter(1)
    assert result == '1'

def test_two_should_return_two(fizzBuzz):
    result = fizzBuzz.filter(2)
    assert result == '2'

@pytest.mark.skip(reason="WIP")
def test_three_should_return_fizz(fizzBuzz):
    result = fizzBuzz.filter(3)
    assert result == 'Fizz'

class FizzBuzz:
	
    def filter(self, number):
        return str(number)