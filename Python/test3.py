# %%
def gcd(a, b):
    return gcd(b, a % b) if b != 0 else a
    # 找最大公因數 這事標準的輾轉相除法


class Rational:
    def __init__(self, a: int, b: int):
        # b分之a
        self.a = a
        self.b = b

    def add(self, other):
        # 兩個自然數的加法
        # a/b + c/d = (ad + bc)/bd
        na = self.a * other.b + self.b * other.a
        nb = self.b * other.b
        g = gcd(na, nb)
        return rational_number(na // g, nb // g)

    def __add__(self, other):
        # 兩個自然數的加法
        # a/b + c/d = (ad + bc)/bd
        na = self.a * other.b + self.b * other.a
        nb = self.b * other.b
        g = gcd(na, nb)
        return rational_number(na // g, nb // g)

    def __sub__(self, other):
        # a/b - c/d = (ad - bc)/bd
        na = self.a * other.b - self.b * other.a
        nb = self.b * other.b
        g = gcd(na, nb)
        return rational_number(na // g, nb // g)

    def prod(self, other):
        # a/b * c/d = ac/bd 乘法
        na = self.a * other.a
        nb = self.b * other.b
        g = gcd(na, nb)
        return rational_number(na // g, nb // g)

    def __mul__(self, other):
        # a/b * c/d = ac/bd 乘法
        na = self.a * other.a
        nb = self.b * other.b
        g = gcd(na, nb)
        return rational_number(na // g, nb // g)

    def __truediv__(self, other):
        # a/b / c/d = ad/bc  除法
        na = self.a * other.b
        nb = self.b * other.a
        g = gcd(na, nb)
        return rational_number(na // g, nb // g)

    def __str__(self):
        return f"{self.a}/{self.b}"
