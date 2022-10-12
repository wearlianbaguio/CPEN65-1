class Circle:
    def __init__(self, pi, r):  # "pi" is "π", a special character which is not readable by phython
        self.pi = pi
        self.r = r

    def Area(self):
        print("Area of Circle =", self.pi * self.r ** 2)  # The formula for the area is πr^2.

    def Area2(self):
        print("Area of Circle Using Diameter =", ((( self.r * 2) ** 2)* self.pi)/4)  # The formula for this area is (π2r^2)/4 for the diamater "2r=diameter".

circ = Circle(3.14, 55)  # we all know that pi/π is an infinite decimal, thus I put 3.14 as the approximate value for it.
circ.Area()
circ.Area2()