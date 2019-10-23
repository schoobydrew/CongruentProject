#fraction class to handle fractions
class Fraction:
    #denominator cant = 0
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator if denominator != 0 else 1
    def __repr__(self):
        return "{numerator}/{denominator}".format(numerator=self.num, denominator=self.den)
