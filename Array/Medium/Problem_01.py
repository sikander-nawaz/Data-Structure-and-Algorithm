# // Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# // We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# // You must solve this problem without using the library's sort function.

# // Example 1:
# // Input: nums = [2,0,2,1,1,0]
# // Output: [0,0,1,1,2,2]

# // SOLUTION:

class Solution:
    def sortColors(self, nums):
        red = 0
        white = 0
        blue = 0

        for val in nums:
            if val == 0:
                red += 1
            elif val == 1:
                white += 1
            else:
                blue += 1

        i = 0
        for j in range(red):
            nums[i] = 0
            i += 1
        for j in range(white):
            nums[i] = 1
            i += 1
        for j in range(blue):
            nums[i] = 2
            i += 1

        return nums




