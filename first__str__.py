def __init__(self, numerator, denominator):

        self.numerator = numerator
        self.denominator = denominator

def __str__(self):
        if self.numerator%self.denominator == 0:
            return f"{int(self.numerator/self.denominator)}"
        else:
            a = self.numerator
            b = self.denominator
            while b != 0:
                helpful=b
                b=a%b
                a=helpful 
            self.numerator = int(self.numerator/abs(helpful))
            self.denominator = int(self.denominator/abs(helpful))
            return f"{self.numerator}/{self.denominator}"

    

#### nietolerancja float ####



    if numerator % denominator == 0:
            self.numerator = int(numerator/denominator)
            self.denominator = 1
        else:
            a = numerator
            b = denominator
            while b != 0:
                helpful=b
                b=a%b
                a=helpful 
            self.numerator = int(numerator/abs(helpful))
            self.denominator = int(denominator/abs(helpful))
            print("koniec",)
        