def exchange_money(budget: float, exchange_rate: float) -> float:
    """Estimates value of currency after exchange

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.

    Function that takes the amount of money you are planning to exchange and the unit value of the foreign currency and returns the value in the foreign currency.
    """

    return budget/exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    """Calculates the currency left after an exchange

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.

    Function that takes the amount of money you own and the amount of your money you want to exchange now and returns the amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """Calculates the value of bills

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.

    Function that takes the value of a bill and the amount of bills you received and returns the total value of bills you now have.
    """

    return denomination * number_of_bills


def get_number_of_bills(budget: float, denomination: int) -> int:
    """Calculate the number of bills you can exchange

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.

    Function that takes the amount of money you are planning to exchange and the value of a single bill and returns the number of bills after exchanging all your money.
    """

    return int(budget//denomination)


def get_leftover_of_bills(budget: float, denomination: int) -> float:
    """Calculate the leftover amount that cannot be exchanged given the current denomination

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.

    Function that takes the amount of money you are planning to exchange and the value of a single bill and returns the leftover amount that cannot be exchanged given the current denomination.
    """

    return budget % denomination


def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int:
    """Calculate the maximum value you can get after exchange

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.

    Function that takes the amount of your money you are planning to exchange, the unit value of the foreign currency, the percentage that is taken as an exchange fee and the value of a single bill and returns the maximum value you can get.
    """
    actual_exchange_rate = exchange_rate + ((spread/100) * exchange_rate)
    exchanged_value = exchange_money(budget, actual_exchange_rate)
    number_of_bills = get_number_of_bills(exchanged_value, denomination)
    return number_of_bills * int(denomination)
