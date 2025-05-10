# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# nums=[1,1,2]
# sets=set({})
# for i in nums:
#     sets.add(i)
# k=len(sets)
# output=[]
# for i in sets:
#     output.append(i)
# print(len(output),",",(output))
nums=[1,1,2]
k=0
count=0
for i in range(0,len(nums)-1):
    j=i+1
    for j in range(j,len(nums)-1):
        if nums[i]==nums[j]:
            nums.remove((nums[j]))
            count=+1
        j=+1
print(nums)        
k=len(nums)   
ans=f"{k} , nums ={nums}"    
print(ans) 



