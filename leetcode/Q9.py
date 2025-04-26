# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.


x=int(input("enter="))
st=str(x)
rev=st[-1 ::-1]
print(rev)
if st==rev:
    print(True)
else:
    print(False)