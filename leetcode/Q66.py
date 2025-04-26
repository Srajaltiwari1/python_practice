# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:
digits=[1,2,3]
sum=""
for i in digits:
    st=str(i)
    sum=sum+st
print(sum)
add=int(sum)
add=add+1
st_1=str(add)
main_l=[]
for i in st_1:
    main_l.append(int(i))
print(main_l)