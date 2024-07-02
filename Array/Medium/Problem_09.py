# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
 
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# SOLUTION:


def longestConsecutive(nums):
     longest = 0
     numsSet = set(nums)
     for i in numsSet:
          if (i - 1) not in numsSet:
               count = 1
               while (i + count) in numsSet:
                    count += 1
               longest = max(longest, count)
     return longest

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))