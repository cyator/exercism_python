def square(number: int) -> int:
    """Calculate the number of grains on a given square of a chessboard.

    :param number: int - the number of the square
    :return: int - the number of grains on the given square

    Function that takes the number of the square and returns the number of grains on the given square.
    """
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")

    return 2 ** (number-1)


def total() -> int:
    """Calculate the total number of grains on the chessboard.

    :return: int - the total number of grains on the chessboard

    Function that returns the total number of grains on the chessboard.
    """

    return 2 ** 64 - 1
