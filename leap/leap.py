def leap_year(year: int):
    """Checks if a year is a leap year.
    :param: int - the year to check
    :return: bool - True if year is a leap year, False otherwise 

    Function that takes a year and returns True if the year is a leap year, False otherwise.
    """

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
