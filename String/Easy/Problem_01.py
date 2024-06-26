# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

# Example 1:
# Input: word = "USA"
# Output: true\

# SOLUTION:

def detectCapitalUse(word):
     return word.isupper() or word.islower() or word.istitle()

word = "USA"
detectCapitalUse(word)