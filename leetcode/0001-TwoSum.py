#   Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#   You may assume that each input would have exactly one solution, and you may not use the same element twice.
#   You can return the answer in any order.
#   
#   Example 1:
#   Input: nums = [2,7,11,15], target = 9
#   Output: [0,1]
#   Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#   
#   Example 2:
#   Input: nums = [3,2,4], target = 6
#   Output: [1,2]
#   
#   Example 3:
#   Input: nums = [3,3], target = 6
#   Output: [0,1]
#   
#   Constraints:
#       2 <= nums.length <= 104
#       -109 <= nums[i] <= 109
#       -109 <= target <= 109
#       Only one valid answer exists.
#   
#   Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

def twoSum(nums: list[int], target: int) -> list[int]:
    # Solution with O(n^2) complexity
#    for i in range(0, len(nums)):
#        for j in range(0, len(nums)):
#            if nums[i]+nums[j] == target and i != j:
#                return [i, j]
    # Solution with O(n logn) complexity
#    nums_backup = nums.copy()
#    nums.sort()
#    i = 0
#    j = len(nums)-1
#    while True:
#        if nums[i] + nums[j] == target:
#            res = []
#            for k in range(0, len(nums_backup)):
#                if nums_backup[k] == nums[i]:
#                    if k not in res: res.append(k)
#                if nums_backup[k] == nums[j]:
#                    if k not in res: res.append(k)
#            return res
#        if nums[i] + nums[j] < target:
#            i += 1
#        if nums[i] + nums[j] > target:
#            j -= 1
    # Solution with O(n) complexity
    rev_table = {}
    for i in range(len(nums)):
        second_addend = target - nums[i]
        if second_addend in rev_table:
       		return [rev_table[second_addend], i]
       	else:
       		rev_table[nums[i]] = i


a = [2,7,11,15]
t = 18
# Output: [0,1]
print(twoSum(a, t))