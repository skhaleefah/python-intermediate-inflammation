"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean
from inflammation.models import daily_max



# def test_daily_mean_zeros():
#     """Test that mean function works for an array of zeros."""
    

#     test_input = np.array([[0, 0],
#                            [0, 0],
#                            [0, 0]])
#     test_result = np.array([0, 0])

#     # Need to use Numpy testing functions to compare arrays
#     npt.assert_array_equal(daily_mean(test_input), test_result)


# def test_daily_mean_integers():
#     """Test that mean function works for an array of positive integers."""

#     test_input = np.array([[1, 2],
#                            [3, 4],
#                            [5, 6]])
#     test_result = np.array([3, 4])

#     # Need to use Numpy testing functions to compare arrays
#     npt.assert_array_equal(daily_mean(test_input), test_result)

# def test_daily_max_integers():
#     """Test that max function works for an array of positive integers"""

#     test_input = np.array([[1, 2],
#                            [3, 4],
#                            [5, 6]])
#     test_result = np.array([5,6])
#     # Need to use Numpy testing functions to compare arrays
#     npt.assert_array_equal(daily_max(test_input), test_result)


def test_daily_max_string():
    """ Test for TypeError when parsing strings with daily_max function """

    with pytest.raises(TypeError):
        error_expected = daily_max(['Hello', 'there'])


def test_daily_mean_string():
    """ Test for TypeError when parsing strings with daily_mean function """

    with pytest.raises(TypeError):
        error_expected = daily_mean(['Hello', 'there'])


## instead of writing test functions for every function like this one by one, we can modularize 
## and create a single function which takes the functions as inputs. Instead of having a function
## for zeroes and a function for integers, we write a single function which can do both. 



# The wrapper applies to the function directly below it. It's like a way of defining a variable temporarily. The wrapper will 
# tell the function below it that these are the pairs "test_input" and "test_result" and it will feed all of these pairs into the 
# function directly below it. The arguments of that function should be the same as the keys in this wrapper/decoration. 

@pytest.mark.parametrize(
        "test_input, test_result",
        [
            ([[0,0], [0,0], [0,0]], [0,0]),
            ([[1,2], [3,4], [5,6]], [3,4]),
            (np.zeros((3,5)), np.zeros(5))
        ]
)

def test_daily_mean(test_input, test_result):
    """ Test that mean function works for both zeroes and integers """
    npt.assert_array_equal(daily_mean(test_input), test_result)


@pytest.mark.parametrize(
        "test_input, test_result",
        [
            ([[0,0], [0,0], [0,0]], [0,0]),
            ([[1,2], [3,4], [5,6]], [5,6]),
            (np.zeros((3,5)), np.zeros(5))
        ]
)

def test_daily_max(test_input, test_result):
    """ Test that max function works for both zeroes and integers """
    npt.assert_array_equal(daily_max(test_input), test_result)

