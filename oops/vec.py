class two_D_vector():
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def vec2D(self):
        print(f"heyy!!!,the vector is  {self.i} X {self.j} ")
    
class three_D_vector(two_D_vector):
    def __init__(self,k):
        self.k=k
    def vec3D(self):
        print(f"heyy!!!,the vector is {self.i}X{self.j}X{self.k}")

s=three_D_vector(2,3,4)
print(s.i,s.j,s.k)

 
