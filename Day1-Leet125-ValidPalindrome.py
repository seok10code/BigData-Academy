Solution 1.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs)>1:
            if strs.pop(0) != strs.pop():
                return False
        return True
        
        
        
        
  Solution 2. (using deque)
  
  class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs : Deque = collections.deque()
        
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
                
        while len(strs)>1:
            if strs.popleft() != strs.pop():
                return False
        return True

  
  
  
  
