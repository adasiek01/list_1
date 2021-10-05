class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def printing(self):
        return f"{self.num}/{self.den}"

    def __add__(self, f2):
        result = (self.num * f2.den + f2.num * self.den)/(self.den * f2.den)
        return result

    def __sub__(self, f2):
        result = (self.num * f2.den - f2.num * self.den)/(self.den * f2.den)
        return result

    def __mul__(self, f2):
        result = (self.num * f2.num)/(self.den * f2.den)
        return result

    def __truediv__(self, f2):
        result = (self.num * f2.den)/(self.den * f2.num)
        return result

    def getNum(self):
        return self.num

    def getDem(self):
        return self.den

#f1 = Fraction(1, 5)
#print(f1.printing())
#print((Fraction(1, 3) + Fraction(1, 2)))
#print((Fraction(1, 3) / Fraction(1, 2)))
#print(f1.getDem())