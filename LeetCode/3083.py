class Solution(object):
    def isSubstringPresent(self, s: str) -> bool:
        
         for i in range(len(s) - 1):
            
            substring = s[i:i+2]
            
            if substring in s[::-1]:
                return True
                
         return False







