import random
r=random.randrange(101)
for i in range(50):
 a=int(input("enter the num"))
 
 if(a==r):
  print("correct!!!")
  break
 elif(a>r):
     print(" your num is too big!!! ")
     
 elif(a<r):
    print("your num is too small!!!")
    
 else:
    print("try again")
 

