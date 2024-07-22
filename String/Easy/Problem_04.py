# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.
# For each index i, names[i] and heights[i] denote the name and height of the ith person.
# Return names sorted in descending order by the people's heights.

# Example 1:
# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: Mary is the tallest, followed by Emma and John.

# SOLUTION:

def sortPeople(names, heights):
     sorted_people = sorted(zip(heights, names), reverse=True)
     sorted_names = [name for height, name in sorted_people]
     return sorted_names
