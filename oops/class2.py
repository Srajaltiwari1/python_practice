class calculator():
    def __init__(self,n):
        self.n=n
    def square(self):
        print(self.n**2)
    def cube(self):
        print(self.n**3)
    def root(self):
        print(self.n**0.5)
    @staticmethod
    def nam():
        print("hellow")
squ=calculator(4)
squ.square()
squ.cube()
squ.root()
squ.nam()