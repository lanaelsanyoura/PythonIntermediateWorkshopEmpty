"""
Mini examples of recursive functions
"""


def factorial(n):
    """
    Return n! where n! = n* (n-1) * (n-2) * (n-3)...*1
    @param n:
    @return: n!
    """
    pass


def factorial_iterative(n):
    """
    Iteratively compute the factorial
    :param n: the value we are computing the factorial of
    :return: n!
    """
    pass


def fibonacci(n):
    """
    Return the fibonnaci of this n where
    fibonacci(n) = fibonacci(n - 1 ) + fibonacci(n - 2)
    and fibonacci(0) = fibonacci(1) = 1
    @param n:
    @return:fibonancci(n)
    """
    pass


def pizzaParty(n):
    """
    How many slices of pizza do we need if every person will eat double
    what the one behind them ate + exactly what the person two behind
    them ate.
    Assume the first person will always eat 1 slice and the second person will always eat 2
    :return:
    """
    pass


def sum_list(lists):
    """
    Given an arbitrarily levelled list, return the sum of all its elements
    Hint, isinstance(n, int) returns true if the type of n is an int
    >>> sum_list([1,[2,[3,4],5],6])
    21
    >>> sum_list([1,2,3])
    6

    @param lists:
    @return: sum of the elements in this list
    """
    pass


def max_list(lists):
    """
    Given an arbitrarily levelled list, return the max of all its elements
    Hint, isinstance(n, int) returns true if the type of n is an int
    >>> max_list([1,[2,[3,4],5],6])
    6
    >>> sum_list([1,2,3])
    3

    @param lists:
    @return:
    """
    pass


def recursive(variable):
    # The Base Case:
    # if (variable ...)
    # the simplest form of our variable
    # Where return of recursive(variable) is independently defined
    # (else)
    # return recursive( ... )
    pass
