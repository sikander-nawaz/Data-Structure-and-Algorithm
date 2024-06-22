# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
# Example 1:
# Input: s = "()"
# Output: true

# SOLUTION:

def isValid(self, s: str) -> bool:
     res=[]
     if(s[0]==")" or s[0]=="}" or s[0]=="]"):
          return False
     for i in s:
          if(i=="(" or i=="{" or i=="["):
               res.append(i)
          elif(len(res)!=0 and (res[-1]=="(" or res[-1]=="{" or res[-1]=="[")):
               if((i==")" and res[-1]=="(") or (i=="}" and res[-1]=="{") or (i=="]" and res[-1]=="[")):
                    res.pop()

               else:
                    return False
          else:
               return False
        
          if(len(res)==0):
               return True
     return False
