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
k = 1  # index for placing next unique element
for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
        nums[k] = nums[i]
        k += 1
print(k)