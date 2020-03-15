import functools


def square_of_sum(number):
    sums = sum(list(range(1, number+1)))
    return sums ** 2


def sum_of_squares(number):
    nums = list(range(1, number+1))
    sums = sum(map(lambda a: a**2, nums))
    return sums


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
