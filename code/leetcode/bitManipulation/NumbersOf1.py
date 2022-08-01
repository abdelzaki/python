"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
"""

class Solution:
    def hammingWeight(n: int) -> int:
        count : int = 0
        while n:
            if n % 2:
                count += 1
            n = n >> 1
        return count
    
    
n  = 0b00000000001011
print(Solution.hammingWeight(n))