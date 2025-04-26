import random
l=["r","p","c"]
for i in range(30):
 a=random.randrange(3)
 c=l[a]
 b=input("enter : ")
 print(c)
 if(b==c):
  print("tie")
  break
 elif(b=="r" and c=="p"):
  print("u lost")
  break
 elif(b=="r" and c=="c"):
  print("u won")
  break
 elif(b=="p" and c=="r"):
  print("u won")
  break
 elif(b=="p" and c=="c"):
  print("u lost")
  break
 elif(b=="c" and c=="p"):
  print("u won")
  break
 elif(b=="c" and c=="r"):
  print("u lost")
  break
 else:
  print("none!!!!")