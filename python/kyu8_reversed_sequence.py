"""
Get the number n (n>0) to return the reversed sequence from n to 1
"""


def reverse_seq(n):
    """
    :param n: positive integer value
    :return: sequence (list) from given value to 1
    """
    count = 0
    seq = []
    while count >= 1:
        seq.append(count)
        count -= 1
    return seq
