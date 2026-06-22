class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x  #to keep the original number safe. because after while loop processing x will end up being some other number. so num will hold its initia value 
        
        rev = 0
        while x > 0:
            rev = rev * 10 + x % 10
            x = x // 10

        if rev == num:
            return True
        else: 
            return False
        