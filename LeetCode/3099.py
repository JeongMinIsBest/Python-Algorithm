class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:

        harshad = sum(int(digit) for digit in str(x))

        if x % harshad == 0:
             return harshad
        else:
            return -1
        
