def add():
    name=input("enter your username")
    passw=input("enter the password")
    
    with open('password.txt','a') as f:
     f.write(name + "|" + passw +"\n")

   
pwd=input("what is thr master password ")
if(pwd=="#"):
    print('''correct!!!''')
    a=input("press add for adding password and view for seeing password")
    if(a=="add"):
       add()
    
else:
    print("master password is wrong")
   
