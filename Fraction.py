import numpy
#fraction class to handle fractions
class Fraction:
    #denominator cant = 0
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator if denominator != 0 else 1
    def __repr__(self):
        return "{numerator}/{denominator}".format(numerator=self.num, denominator=self.den)
    def simplify(self):
        gcd = numpy.gcd(self.num, self.den)
        self.num //= gcd
        self.den //= gcd
    #takes in another Fraction
    def __mul__(self, value):
        return Fraction(self.num*value.num, self.den*value.den)
    #fraction is congruent to ? mod m
    def fraction2Int(self, m):
        pass
