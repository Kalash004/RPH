class ComplexNumber:
    def init(self, re, im):
        self.re = re;
        self.im = im;

    def __repr__(self):
        return f"{self.re}+{self.im}i";

    def __abs__(self):
        math.sqrt(math.pow(self.re) + math.pow(self.im));

    def inc(self, re_koef, im_koef):
        self.re += re_koef;
        self.im += im_koef;

    def 