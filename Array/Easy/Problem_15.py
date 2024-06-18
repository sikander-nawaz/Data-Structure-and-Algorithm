# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
# Return any answer array that satisfies this condition.

# Example 1:
# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

# SOLUTION:


def sortArrayByParityII(nums):
     odd = []
     even = []
     ans = []
     for i in range(len(nums)):
          if nums[i] % 2 == 0:
               even.append(nums[i])
          else:
               odd.append(nums[i])

     for i in range(len(odd)):
          ans.append(even[i])
          ans.append(odd[i])

     return ans

sortArrayByParityII([4,2,5,7])