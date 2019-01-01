class Fraction:
    """
    A Fraction class that has a numerator and denominator and performs basic
    arithmetic operations
    """

    def __init__(self, numerator, denominator):
        """

        :param numerator: int
        :param denominator: int
        :return:
        """
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        """
        Add this fraction to another
        :param other: Fraction
        :return: Fraction
        """
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def getSimplified(self):
        """
        Return the simplified version of this fraction
        :return:
        """
        gcd = self.gcd_helper(self.numerator, self.denominator)

        return Fraction(self.numerator // gcd, self.denominator // gcd)

    def gcd_helper(self, num, den):
        if den == 0:
            return num
        return self.gcd_helper(den, num % den)

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)

    def __ge__(self, other):
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __le__(self, other):
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __eq__(self, other):
        self_simplified = self.getSimplified()
        other_simplified = other.getSimplified()
        return self_simplified.numerator == other_simplified.numerator and \
               self_simplified.denominator == other_simplified.denominator


if __name__ == '__main__':
    f1 = Fraction(6, 18)

    # Add Fractions Together:
    f2 = Fraction(1, 3)
    sumFraction = f1 + f2
    print(sumFraction)

    # Simplify Fractions:
    print(sumFraction.getSimplified())

    # Compare the fractions
    print(f1 == f2)
