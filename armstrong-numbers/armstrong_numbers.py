def is_armstrong_number(number: int) -> bool:
    """Checks if number is armstrong number
    :param number: int- number to check
    :return: bool - True if number is armstrong number, False otherwise
    Function that takes a number and returns True if the number is an Armstrong number, False otherwise.
    """
    num_str = str(number)

    return number == sum(int(i) ** len(num_str) for i in num_str)
