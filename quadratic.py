class Quadratic:
    """docstring for Quadratic."""
    symbol_sign = [" ", "=", " y", "Y", "x", "X", "+", "-", "*", "/"]
    symbol_numeric = ["0", "1", "2", "3", "4", "5", "6", "7" , "8", "9", "."]
    def __init__(self, equation):
        self.authenticated = False
        self.eq = equation
        self.data = {"X":0, "Y":0, "C":0, "point":[]}
        self.setup()


    def setup(self):
        self.authenticated = self.authenticate_equation()
        if self.authenticated:
            self.data["X"] = self.extract_x()
            self.data["Y"] = self.extract_y()
            self.data["C"] = self.extract_c()

    def authenticate_equation(self):
        c=False
        for i in self.eq:
            c = True
            if i not in (Quadratic("").symbol_sign + Quadratic("").symbol_numeric):
                c = False
                break
        return c

    def extract_num(self,l):
        number_found=0
        a=""
        for i in  l:
            if i not in Quadratic("").symbol_numeric and number_found==0:
                continue
            elif i in Quadratic("").symbol_numeric:
                a+=i
                number_founnd=1

        return float(int(float(a)*10000))/10000

    def extract_x(self):
        return  self.extract_num((self.get_equation().split("=")[1]).split(self.get_equation()[self.get_equation().index("X")+1])[0])

    def extract_y(self):
        return self.extract_num(self.get_equation().split("=")[0])

    def extract_c(self):
        return  self.extract_num((self.get_equation().split("=")[1]).split(self.get_equation()[self.get_equation().index("X")+1])[1])


    def get_equation(self):
        return self.eq

    def text(self):
        print self.data["X"],self.data["Y"],self.data["C"]




ob = Quadratic("1Y=0.45X+0.35")
ob.text()
