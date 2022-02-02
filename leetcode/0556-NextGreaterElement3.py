# Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.
# Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.
# 
# Example 1:
# Input: n = 12
# Output: 21
# 
# Example 2:
# Input: n = 21
# Output: -1
# 
# Constraints:
#     1 <= n <= 231 - 1
def nextGreaterElement(n):
    def exact_digits(n, m):
        d1 = {}
        d2 = {}
        n = str(n)
        m = str(m)
        for e in n:
            d1[e] = d1.get(e, 0) + 1
        for e in m:
            d2[e] = d2.get(e, 0) + 1
        return d1 == d2
    
    digits = list(str(n))
    i = len(digits) - 1
    while i-1 >= 0 and digits[i] <= digits[i-1]:
        i -= 1
        
    if i == 0: return -1

    res = n
    while True:
        res += 1
        if exact_digits(n, res):
            return res if res < 1<<31 else -1

    

print(2**32)
print(nextGreaterElement(99))