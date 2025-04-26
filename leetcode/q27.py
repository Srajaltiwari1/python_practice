# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
nums=[3,2,2,3]
val=3
new_lis=[]
count=0
underSc="_"
for i in nums:
    if i != val:
        new_lis.append(i)
    else:
       count=count+1
lent=len(new_lis)
for i in range(count):
    new_lis.append(int(chr(95)))
print(f"{lent} , nums = {new_lis}")

    
        
