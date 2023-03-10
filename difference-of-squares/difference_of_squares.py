def square_of_sum(number: int) -> int:
    """Calculate the square of the sum of the first n natural numbers.
    :param number: int - the number of natural numbers to sum
    :return: int - the square of the sum of the first n natural numbers using sum = n * (n + 1) / 2

    Function that takes the number of natural numbers to sum and returns the square of the sum of the first n natural numbers.
    """

    return ((number * (number+1)) >> 1) ** 2


def sum_of_squares(number: int) -> int:
    """Calculate the sum of the squares of the first n natural numbers.
    :param number: int - the number of natural numbers to square
    :return: int - the sum of the squares of the first n natural numbers using Faulhaber's formula (n * (n+1) * (2n+1) / 6)

    Function that takes the number of natural numbers to square and returns the sum of the squares of the first n natural numbers.
    """

    return (number * (number + 1) * (2*number+1))/6


def difference_of_squares(number: int) -> int:
    """Calculate the difference between the square of the sum and the sum of the squares of the first n natural numbers.
    :param number: int - the number of natural numbers 
    :return: int - the difference between the square of the sum and the sum of the squares of the first n natural numbers

    Function that takes the number of natural numbers and returns the difference between the square of the sum and the sum of the squares of the first n natural numbers.
    """
    return square_of_sum(number)-sum_of_squares(number)
