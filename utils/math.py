import cmath

class Quadratic:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.d = d = (b ** 2) - (4 * a * c)
        self.sol1 = ((-b - cmath.sqrt(self.d)) / (2 * a)).real
        self.sol2 = ((-b + cmath.sqrt(self.d)) / (2 * a)).real


    def get_positive_result(self):
        return self.sol1 if self.sol1 > 0 else self.sol2

