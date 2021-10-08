class Fraction():

#1

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        #self._representation = f"{str(self.numerator)}/{str(self.denominator)}"

    #def __new__(cls, numerator, denominator):
     #   return f"{str(numerator)}/{str(denominator)}"

    def __add__(self,other): 
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator 
        return f"{new_numerator}/{new_denominator}"

    def __sub__(self,other): 
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator 
        return f"{new_numerator}/{new_denominator}"


    def __mul__(self,other): 
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator 
        return f"{new_numerator}/{new_denominator}"

    def __truediv__(self,other): 
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator 
        return f"{new_numerator}/{new_denominator}"

#2

    def get_num(self):
        return self.numerator
    
    def get_den(self):
        return self.denominator


    
f1 = Fraction(9,2)
print(f1.numerator)
f2=Fraction(1,4)
print(f2)
#print(f1 / f2)

print(f2.get_den())