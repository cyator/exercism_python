def is_triangle(sides: list[int]) -> bool:
    """Checks if is triangle

    :param sides: list[int]- list of sides
    :return: bool - True if  is triangle, False otherwise

    For a shape to be a triangle at all, all sides have to be of length > 0, and the sum of the lengths of any two sides must be greater than or equal to the length of the third side.
    """
    max_side = max(sides)
    return len(sides) == 3 and all(sides) and sum(sides) - max_side >= max_side


def equilateral(sides: list[int]) -> bool:
    """Checks if is equilateral

    :param sides: list[int]- list of sides
    :return: bool - True if  is equilateral, False otherwise

    An equilateral triangle has all three sides the same length.
    """
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides: list[int]) -> bool:
    """Checks if is isosceles

    :param: list[int] - True if is isosceles, False otherwise

    An isosceles triangle has at least two sides the same length.
    """
    return is_triangle(sides) and len(set(sides)) <= 2


def scalene(sides: list[int]) -> bool:
    """Checks if is scalene

    :param: list[int] - True if is scalene, False otherwise
    :return: bool - True if is scalene, False otherwise

    A scalene triangle has all sides of different lengths.
    """
    return is_triangle(sides) and len(set(sides)) == 3
