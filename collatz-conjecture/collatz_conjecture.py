def steps(number: int) -> int:
    """Calculates the number of steps required to reach 1. 

    :param: int - the number n > 0 to start with
    :return: int - the number of steps required to reach 1

    Given a positive integer n, applies the following process repeatedly
    until reaching the value 1:

    - If n is even, divide it by 2 to get n / 2.
    - If n is odd, multiply it by 3 and add 1 to get 3n + 1.

    The conjecture states that no matter which number you start with, you will always reach 1 eventually.
    """

    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    count = 0
    while number != 1:
        if number & 1 == 0:
            number = number >> 1
        else:
            number = number * 3 + 1
        count += 1

    return count
