import math
from typing_extensions import final

class Fraction():

################# 1 #################

    def __init__(self, numerator, denominator):

        #self.numerator = numerator
        #self.denominator = denominator
################# 7 #################

        ### Addition to ex. 1 ###
        def reduce(n,d):
            if n % d == 0:
                n = int(n/d)
                d = 1
            else:
                a = n
                b = d
                while b != 0:
                    helpful=b
                    b=a%b
                    a=helpful 
                n = int(n/abs(helpful))
                d = int(d/abs(helpful))
                return [n,d]

        def transform(k):
            integral = int(math.modf(k)[1])
            help = str(k)
            decimal_index = help.index(".")
            quantity_after_decimal = len(help)-(decimal_index+1)
            decimal_part = int(help[decimal_index+1:])
            k_numerator = integral * 10**quantity_after_decimal + decimal_part
            k_denominator = 10**quantity_after_decimal
            #return [k_numerator,k_denominator]
            reduced = reduce(k_numerator,k_denominator)
            return reduced

        if type(numerator) == int and type(denominator) == int:
            self.numerator = numerator
            self.denominator = denominator
        elif type(numerator) == float and type(denominator) == int:
            fraction = transform(numerator)
            print("fraction",fraction)
            self.numerator = fraction[0]
            self.denominator = fraction[1]*denominator
            print("den",self.denominator)
            print("num",self.numerator)
        elif type(numerator) == int and type(denominator) == float:
            fraction = transform(denominator)
            self.numerator = numerator * fraction[1]
            self.denominator = fraction[0]
        elif type(numerator) == float and type(denominator) == float:
            fraction_1 = transform(numerator)
            fraction_2 = transform(denominator)
            self.numerator = fraction_1[0]*fraction_2[1]
            self.denominator = fraction_1[1]*fraction_2[0]


        if numerator % denominator == 0:
            self.numerator = int(numerator/denominator)
            self.denominator = 1

        else:
            a = self.numerator
            b = self.denominator
            while b != 0:
                helpful=b
                b=a%b
                a=helpful
            self.numerator = int(self.numerator/abs(helpful))
            self.denominator = int(self.denominator/abs(helpful))


################# 4 #################

        if denominator == 0:
            raise ZeroDivisionError
        #if type(numerator)!=int:
         #   raise Exception("Numerator is not an integer number")
            
        #elif type(denominator)!=int:
         #   raise Exception("Denominator is not an integer number")


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

        

################# 6 #################  
    def __str__(self):
        if self.denominator == 1:
            return f"{self.numerator}"
        else:   
            return f"{self.numerator}/{self.denominator}"

################# 3 #################

    def get_num(self):
        return self.numerator
    
    def get_den(self):
        return self.denominator

################# 2 #################
    def less_than(self,other):
        if self.numerator/self.denominator < other.numerator/other.denominator:
            return True
        else:
            return False

    def more_than(self,other):
        if self.numerator/self.denominator > other.numerator/other.denominator:
            return True
        else:
            return False

    def not_equal(self,other):
        if self.numerator/self.denominator != other.numerator/other.denominator:
            return True
        else:
            return False

    def equal(self,other):
        if self.numerator/self.denominator == other.numerator/other.denominator:
            return True
        else:
            return False

    def less_equal(self,other):
        if self.numerator/self.denominator <= other.numerator/other.denominator:
            return True
        else:
            return False

    def more_equal(self,other):
        if self.numerator/self.denominator >= other.numerator/other.denominator:
            return True
        else:
            return False


################# ADDITIONS #################


    def reduce(self):
        if self.numerator % self.denominator == 0:
            self.numerator = int(self.numerator/self.denominator)
            self.denominator = 1
        else:
            a = self.numerator
            b = self.denominator
            while b != 0:
                helpful=b
                b=a%b
                a=helpful 
            self.numerator = int(self.numerator/abs(helpful))
            self.denominator = int(self.denominator/abs(helpful))


    def split(self):
        number = self.numerator/self.denominator
        integral = int(math.modf(number)[1])
        modulo = abs(self.numerator)%abs(self.denominator)
        return [number, integral, modulo]

    def mixed(self):
        values = self.split()
        if self.numerator % self.denominator == 0:
            return int(self.numerator/self.denominator)
        elif abs(self.numerator) > abs(self.denominator):
            return f"{values[1]} and {values[2]}/{abs(self.denominator)}"
        else:
            if self.numerator*self.denominator > 0:
                return f"{abs(self.numerator)}/{abs(self.denominator)}"
            else:
                return f"{-abs(self.numerator)}/{abs(self.denominator)}"
    
    def plus_integer(self,n):
        extended = n*abs(self.denominator)
        if self.numerator * self.denominator > 0:   
            return f"{abs(self.numerator)+extended}/{abs(self.denominator)}"
        else:
            return f"{-abs(self.numerator)+extended}/{abs(self.denominator)}"

    def plus_float(self,k):
        integral = int(math.modf(k)[1])
        help = str(k)
        decimal_index = help.index(".")
        quantity_after_decimal = len(help)-(decimal_index+1)
        decimal_part = int(help[decimal_index+1:])
        k_numerator = integral * 10**quantity_after_decimal + decimal_part
        k_denominator = 10**quantity_after_decimal
        help_fraction = Fraction(k_numerator,k_denominator)
        help_fraction.reduce()

        total_numerator = help_fraction.numerator * self.denominator + self.numerator * help_fraction.denominator
        total_denominator = help_fraction.denominator * self.denominator
        final_fraction = Fraction(total_numerator, total_denominator)
        return final_fraction


f1 = Fraction(-5,-2)
print(f1)


