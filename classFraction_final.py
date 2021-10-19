import math

def reduce(n, d):
    """
    The method reduces the fraction
    :param n: The numerator
    :param d: The denominator
    :return: Reduced fraction
    """
    if n % d == 0:
        n = int(n/d)
        d = 1
    else:
        a = n
        b = d
        while b != 0:
            helpful = b
            b = a % b
            a = helpful
        if n*d>0:
            n = int(abs(n/helpful))
            d = int(abs(d/helpful))
        else:
            n = int(-abs(n/helpful))
            d = int(abs(d/helpful))
    return [n, d]

def transform(k):
    """
    The method changes float value on fraction
    :param k: String of float characters
    :return: Reduced fraction
    """
    integer = int(math.modf(k)[1])
    string_k = str(k)
    decimal_index = string_k.index(".")
    quantity_after_decimal = len(string_k)-(decimal_index+1)
    if "-" in string_k:
        decimal_part = -int(string_k[decimal_index+1:])
    else:
        decimal_part = int(string_k[decimal_index+1:])
    k_numerator = integer * 10**quantity_after_decimal + decimal_part
    k_denominator = 10**quantity_after_decimal
    reduced = reduce(k_numerator, k_denominator)
    return reduced

class Fraction:

    def __init__(self, numerator, denominator):
        """
        The constructor takes the numerator and denominator of the fraction
        :param numerator: The numerator
        :param denominator: The denominator
        """
        
        if type(numerator) == int and type(denominator) == int:
            reduced = reduce(numerator,denominator)
            self.numerator = reduced[0]
            self.denominator = reduced[1]
        elif type(numerator) == float and type(denominator) == int:
            fraction = transform(numerator)
            self.numerator = fraction[0]
            self.denominator = fraction[1]*denominator
        elif type(numerator) == int and type(denominator) == float:
            fraction = transform(denominator)
            self.numerator = numerator * fraction[1]
            self.denominator = fraction[0]
        elif type(numerator) == float and type(denominator) == float:
            fraction_1 = transform(numerator)
            fraction_2 = transform(denominator)
            self.numerator = fraction_1[0]*fraction_2[1]
            self.denominator = fraction_1[1]*fraction_2[0]

        if self.numerator*self.denominator<0:
            self.denominator = abs(self.denominator)
            self.numerator = -abs(self.numerator)
        else:
            self.denominator = abs(self.denominator)
            self.numerator = abs(self.numerator)


        if denominator == 0:
            raise ZeroDivisionError("Don't divide by zero!")

        """if type(numerator)!=int:
                raise Exception("Numerator is not an integer number")
            
           elif type(denominator)!=int:
               raise Exception("Denominator is not an integer number")"""



    def __add__(self, other):
        """
        The method adds two fractions
        :param other: Second fraction
        :return: Sum
        """
        if type(other)==float:
            fr = transform(other)
            float_numerator = fr[0]
            float_denominator = fr[1]
            new_numerator = self.numerator * float_denominator + self.denominator * float_numerator
            new_denominator = self.denominator * float_denominator 
            return Fraction(new_numerator, new_denominator)

        else:
            new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
            new_denominator = self.denominator * other.denominator 
            return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """
        The method subtracts two fractions
        :param other: Second fraction
        :return: Difference
        """
        if type(other)==float:
            fr = transform(other)
            float_numerator = fr[0]
            float_denominator = fr[1]
            new_numerator = self.numerator * float_denominator - self.denominator * float_numerator
            new_denominator = self.denominator * float_denominator 
            return Fraction(new_numerator, new_denominator)

        else:
            new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
            new_denominator = self.denominator * other.denominator 
            return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        """
        The method multiplies two fractions
        :param other: Second fraction
        :return: Product
        """
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator 
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        """
        The method divides two fractions
        :param other: Second fraction
        :return: Quotient
        """
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator 
        return Fraction(new_numerator, new_denominator)

    def __str__(self):
        """
        The method shows our fraction
        :return: Fraction
        """
        if self.denominator == 1:
            return f"{self.numerator}"
        else:   
            return f"{self.numerator}/{self.denominator}"

    def get_num(self):
        """
        The method shows the numerator of the fraction
        :return: The numerator
        """
        return self.numerator
    
    def get_den(self):
        """
        The method shows the denominator of the fraction
        :return: The denominator
        """
        return self.denominator

    def __lt__(self, other):
        """
        The method checks if the first fraction is smaller than the second
        :param other: Second fraction
        :return: True or False
        """
        if self.numerator/self.denominator < other.numerator/other.denominator:
            return True
        else:
            return False

    def __gt__(self, other):
        """
        The method checks if the first fraction is bigger than the second
        :param other: Second fraction
        :return: True or False
        """
        if self.numerator/self.denominator > other.numerator/other.denominator:
            return True
        else:
            return False

    def __ne__(self, other):
        """
        The method checks if the first fraction is different from the second
        :param other: Second fraction
        :return: True or False
        """
        if self.numerator/self.denominator != other.numerator/other.denominator:
            return True
        else:
            return False

    def __eq__(self, other):
        """
        The method checks if the first fraction is equal to the second
        :param other: Second fraction
        :return: True or False
        """
        if self.numerator/self.denominator == other.numerator/other.denominator:
            return True
        else:
            return False

    def __le__(self, other):
        """
        The method checks if the first fraction is smaller or equal to the second
        :param other: Second fraction
        :return: True or False
        """
        if self.numerator/self.denominator <= other.numerator/other.denominator:
            return True
        else:
            return False

    def __ge__(self, other):
        """
        The method checks if the first fraction is bigger or equal to the second
        :param other: Second fraction
        :return: True or False
        """
        if self.numerator/self.denominator >= other.numerator/other.denominator:
            return True
        else:
            return False

    def mixed(self):
        """
        The method shows clearer version of the fraction
        :return: Clearer fraction
        """
        number = self.numerator/self.denominator
        integer = int(math.modf(number)[1])
        modulo = abs(self.numerator) % abs(self.denominator)

        if self.numerator % self.denominator == 0:
            return int(self.numerator/self.denominator)
        elif abs(self.numerator) > abs(self.denominator):
            return f"{integer} and {modulo}/{abs(self.denominator)}"
        else:
            if self.numerator*self.denominator > 0:
                return f"{abs(self.numerator)}/{abs(self.denominator)}"
            else:
                return f"{-abs(self.numerator)}/{abs(self.denominator)}"
    

    
a = Fraction(5,-2)
b = Fraction(-1,4)

if __name__ == "__main__":
    print(b-1.0)
