class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def printing(self):
        return f"{self.num}/{self.den}"

    def __add__(self, f):
        new_num = (self.num * f.den + f.num * self.den)
        new_den = (self.den * f.den)
        return f"{new_num}/{new_den}"

    def __sub__(self, f):
        new_num = (self.num * f.den - f.num * self.den)
        new_den = (self.den * f.den)
        return f"{new_num}/{new_den}"

    def __mul__(self, f):
        new_num = (self.num * f.num)
        new_den = (self.den * f.den)
        return f"{new_num}/{new_den}"

    def __truediv__(self, f):
        new_num = (self.num * f.den)
        new_den = (self.den * f.num)
        return f"{new_num}/{new_den}"

    def first_bigger(self, f):
        if (self.num/self.den) > (f.num/f.den):
            return True
        else:
            return False

    def first_bigger_or_equal(self, f):
        if (self.num/self.den) >= (f.num/f.den):
            return True
        else:
            return False

    def second_bigger(self, f):
        if (self.num/self.den) < (f.num/f.den):
            return True
        else:
            return False

    def second_bigger_or_equal(self, f):
        if (self.num/self.den) <= (f.num/f.den):
            return True
        else:
            return False

    def equal(self, f):
        if (self.num/self.den) == (f.num/f.den):
            return True
        else:
            return False

    def getNum(self):
        return self.num

    def getDem(self):
        return self.den

    def is_integer(self):
        try:
            isinstance(self.num, int)
        except:
            raise ValueError
        try:
            isinstance(self.den, int)
        except:
            raise ValueError

    def __str__(self):
        for i in range(1, 10):
            if self.num % i == 0 and self.den % i == 0:
                self.num = self.num / i
                self.den = self.den / i
        return f"{self.num}/{self.den}"



f1 = Fraction(-1, 3)
f2 = Fraction(-1, 6)
#print(f1.printing())
#print((Fraction(1, 3) + Fraction(1, 2)))
#print((Fraction(1, 3) / Fraction(1, 2)))
#print(f1.getDem())
#print(f1.equal(f2))
#print(f1.is_integer())
print(Fraction(4, 8).__str__())
f3=f1+f2
print(f3)
