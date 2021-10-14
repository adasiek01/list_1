import math


class Fraction:

    def __init__(self, numerator, denominator):
        """
        The constructor takes the numerator and denominator of the fraction
        :param numerator: The numerator
        :param denominator: The denominator
        """

        self.numerator = numerator
        self.denominator = denominator

        def reduce_init(n, d):
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
                n = int(n/abs(helpful))
                d = int(d/abs(helpful))
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
            decimal_part = int(string_k[decimal_index+1:])
            k_numerator = integer * 10**quantity_after_decimal + decimal_part
            k_denominator = 10**quantity_after_decimal
            reduced = reduce_init(k_numerator, k_denominator)
            return reduced

        if type(numerator) == int and type(denominator) == int:
            self.numerator = numerator
            self.denominator = denominator
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

        if numerator % denominator == 0:
            self.numerator = int(numerator/denominator)
            self.denominator = 1

        else:
            a = self.numerator
            b = self.denominator
            while b != 0:
                helpful = b
                b = a % b
                a = helpful
            if self.numerator*self.denominator>0:
                self.numerator = int(abs(self.numerator/helpful))
                self.denominator = int(abs(self.denominator/helpful))
            else:
                self.numerator = int(-abs(self.numerator/helpful))
                self.denominator = int(abs(self.denominator/helpful))

        if denominator == 0:
            raise ZeroDivisionError
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
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator 
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """
        The method subtracts two fractions
        :param other: Second fraction
        :return: Difference
        """
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

    def less_than(self, other):
        """
        The method checks if the first fraction is smaller than the second
        :param other: Second fraction
        :return: True or False
        """
        if self.numerator/self.denominator < other.numerator/other.denominator:
            return True
        else:
            return False

    def more_than(self, other):
        """
        The method checks if the first fraction is bigger than the second
        :param other: Second fraction
        :return: True or False
        """
        if self.numerator/self.denominator > other.numerator/other.denominator:
            return True
        else:
            return False

    def not_equal(self, other):
        """
        The method checks if the first fraction is different from the second
        :param other: Second fraction
        :return: True or False
        """
        if self.numerator/self.denominator != other.numerator/other.denominator:
            return True
        else:
            return False

    def equal(self, other):
        """
        The method checks if the first fraction is equal to the second
        :param other: Second fraction
        :return: True or False
        """
        if self.numerator/self.denominator == other.numerator/other.denominator:
            return True
        else:
            return False

    def less_equal(self, other):
        """
        The method checks if the first fraction is smaller or equal to the second
        :param other: Second fraction
        :return: True or False
        """
        if self.numerator/self.denominator <= other.numerator/other.denominator:
            return True
        else:
            return False

    def more_equal(self, other):
        """
        The method checks if the first fraction is bigger or equal to the second
        :param other: Second fraction
        :return: True or False
        """
        if self.numerator/self.denominator >= other.numerator/other.denominator:
            return True
        else:
            return False

    def reduce(self):
        """
        The method reduces the fraction
        """
        if self.numerator % self.denominator == 0:
            self.numerator = int(self.numerator/self.denominator)
            self.denominator = 1
        else:
            a = self.numerator
            b = self.denominator
            while b != 0:
                helpful = b
                b = a % b
                a = helpful
            self.numerator = int(self.numerator/abs(helpful))
            self.denominator = int(self.denominator/abs(helpful))

    def split(self):
        """
        The method extracts fraction, integral part and modulo of our fraction
        :return: List of fraction, integral part and modulo
        """
        number = self.numerator/self.denominator
        integer = int(math.modf(number)[1])
        modulo = abs(self.numerator) % abs(self.denominator)
        return [number, integer, modulo]

    def mixed(self):
        """
        The method shows clearer version of the fraction
        :return: Clearer fraction
        """
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
    
    def plus_integer(self, n: int):
        """
        The method adds integer to the fraction
        :param n: Integer
        :return: Sum
        """
        extended = n*abs(self.denominator)
        if self.numerator * self.denominator > 0:   
            new_numerator = (abs(self.numerator)+extended)
            new_denominator = abs(self.denominator)
        else:
            new_numerator = (abs(self.numerator)+extended)
            new_denominator = abs(self.denominator) 
        new_fraction = Fraction(new_numerator, new_denominator)
        return new_fraction

    def plus_float(self, k: float):
        """
        The method adds float to the fraction
        :param k: Float
        :return: Sum
        """
        integral = int(math.modf(k)[1])
        string = str(k)
        decimal_index = string.index(".")
        quantity_after_decimal = len(string)-(decimal_index+1)
        
        if int(math.modf(k)[0]) < 0 or int(math.modf(k)[1]) <0:
            decimal_part = -int(string[decimal_index+1:])
        else:
            decimal_part = int(string[decimal_index+1:])

        k_numerator = integral * 10**quantity_after_decimal + decimal_part
        k_denominator = 10**quantity_after_decimal
            
        help_fraction = Fraction(k_numerator, k_denominator)

        total_numerator = help_fraction.numerator * self.denominator + self.numerator * help_fraction.denominator
        total_denominator = help_fraction.denominator * self.denominator
        final_fraction = Fraction(total_numerator, total_denominator)
        return final_fraction
