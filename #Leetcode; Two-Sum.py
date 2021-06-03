# Leetcode; Two-Sum
# William Manning
# 6/3/2021

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Example:
# Input: nums = [2,7,10,34] target = 9
# Output [0,1] as 2+7 = 9


#Note that this solution is O(1) iff you are able to sort the list of numbers.
def twoSumSorted(nums, target):
    nums.sort()
    #O(1) Space Complexity
    start = 0
    end = len(nums)-1
    while(start<end):
        if(nums[start] + nums[end] == target):
            print("1")
            return [start, end]
        elif(nums[start] + nums[end] > target):
            print("2")
            end = end-1
        else:
            print("3")
            start+=1
#This solution is for if you cannot sort the nums
def twoSum(nums, target):
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in nums:
            if(i != nums.index(difference)): #Have to check if it is using the same number twice by mistake
                return [i,nums.index(difference)]
    return []


nums = [2, 7, 10, 34]
target = 9


print(twoSum(target, nums))
