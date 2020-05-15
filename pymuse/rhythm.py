# coding: utf-8


class WrongDivisor(Exception):
    MESSAGE = "Rhythmic signatures has non-multiple divisors ({0} {1})"

    def __init__(self, r1, r2):
        self.message = self.MESSAGE.format(r1.divisor, r2.divisor)

    def __str__(self):
        return self.message


def common_signature(s1, s2):
    """ Get the signature that can bind different signatures together
        It returns a signature with the lesser common multiple between
        given signatures. """
    # TODO: Extend calculation to stacks of signatures
    # Avec une application de l'algorithme du plus petit
    # multiple commun sur un ensemble indéterminé d'entiers naturels
    max_dividend = max(s1.dividend, s2.dividend)
    min_dividend = min(s1.dividend, s2.dividend)
    if max_dividend % min_dividend == 0:
        return Signature(min_dividend, s1.divisor)
    return multiply(s1, s2)


def multiply(s1, s2):
    if s1.divisor == s2.divisor:
        return Signature(s1.dividend * s2.dividend, s1.divisor)
    raise WrongDivisor(s1, s2)


class Signature(object):

    def __init__(self, dividend, divisor):
        self._dividend = dividend
        self._divisor = divisor

    def multiple_of(self, other):
        """ Test if a signature is multiple of another.
            If multiple these signatures can be played together at
            the same tempo without any modification to each """
        if self._divisor % other.divisor == 0:
            return (max(self._dividend, other.dividend) %
                    min(self._dividend, other.dividend)) == 0
        return False

    @property
    def dividend(self):
        return self._dividend

    @property
    def divisor(self):
        return self._divisor

    def __eq__(self, other):
        if self._divisor == other.divisor:
            return self._dividend == other.dividend
        return False

    def __str__(self):
        return "{dividend}/{divisor}".format(dividend=self._dividend,
                                             divisor=self._divisor)
