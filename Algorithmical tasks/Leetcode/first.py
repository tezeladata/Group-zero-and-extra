# Two sum
class Solution(object):
    def twoSum(self, nums, target):
        
        res = []

        for x in range(len(nums)-1):
            for i in range(x+1, len(nums)):
                if nums[x] + nums[i] == target:
                    res.append([x, i])

        updated = []
        for i in res:
            for x in i:
                updated.append(x)
        
        return updated
# or:
class Solution(object):
    def twoSum(self, nums, target):
        
        res = []

        for x in range(len(nums)-1):
            for i in range(x+1, len(nums)):
                if nums[x] + nums[i] == target:
                    res.append(x)
                    res.append(i)
        
        return res
    
# Palindrome number
class Solution(object):
    def isPalindrome(self, x):
        return str(x)[::-1] == str(x)
        
# Valid parentheses
class Solution(object):
    def isValid(self, s):
        matching_parenthesis = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in matching_parenthesis:
                top_element = stack.pop() if stack else '#'
                if matching_parenthesis[char] != top_element:
                    return False
            else:
                stack.append(char)
    
        return not stack
    
# Remove Duplicates from Sorted Array
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
    
        insert_pos = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[insert_pos] = nums[i]
                insert_pos += 1
        
        return insert_pos
    
# Remove element
class Solution(object):
    def removeElement(self, nums, val):
        insert_pos = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        return insert_pos
    
# Length of last word
class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.strip().split(" ")[-1])
    
# Plus one
class Solution(object):
    def plusOne(self, digits):
        return  [int(i) for i in str(int("".join([str(i) for i in digits])) + 1)]
    
# Sqrt(x)
class Solution(object):
    def mySqrt(self, x):
        return int(x**0.5)
    
# Search Insert Position
class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)

        nums.append(target)
        nums.sort()

        return nums.index(target)
    
# Find the Index of the First Occurrence in a String
class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
    
        len_haystack = len(haystack)
        len_needle = len(needle)
        
        for i in range(len_haystack - len_needle + 1):
            if haystack[i:i+len_needle] == needle:
                return i
        
        return -1
    
# Climbing Stairs
class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2

        first = 1
        second = 2

        for i in range(3, n + 1):
            current = first + second
            first = second
            second = current
        
        return second
    
# Valid Palindrome
class Solution(object):
    def isPalindrome(self, s):
        s = "".join([i for i in s.lower() if i.isalnum()])
        return s == s[::-1]
    
# Single Number
class Solution(object):
    def singleNumber(self, nums):
        return [i for i in nums if nums.count(i) == 1][0]
    
# Best Time to Buy and Sell Stock
class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            
            potential_profit = price - min_price
            
            if potential_profit > max_profit:
                max_profit = potential_profit
        
        return max_profit
    
# Add Binary
class Solution(object):
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]
    
# Pascal's Triangle
class Solution(object):
    def generate(self, numRows):
        a = []
        for i in range(numRows):
            a.append([])
            a[i].append(1)
            for j in range(1, i):
                a[i].append(a[i-1][j-1] + a[i-1][j])
            if i > 0: 
                a[i].append(1)
        
        return a
    
# Majority Element
class Solution(object):
    def majorityElement(self, nums):
        for i in list(set(nums)):
            if nums.count(i) > len(nums) * 0.5:
                return i
            
# Happy Number
class Solution(object):
    def isHappy(self, n):
        def convert(value):
            return sum(int(i) ** 2 for i in str(value))

        already = set()

        while n != 1 and n not in already:
            already.add(n)
            n = convert(n)

        return n == 1
    
# Contains Duplicate
class Solution(object):
    def containsDuplicate(self, nums):
        return sorted(nums) != sorted(list(set(nums)))
    
# Contains Duplicate II
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        num_index = {}
        for i, num in enumerate(nums):
            if num in num_index and i - num_index[num] <= k:
                return True
            num_index[num] = i
        return False
    
# Power of Two
class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        
        while n%2 == 0:
            n //= 2
        
        return n == 1
    
# Valid Anagram
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(list(s)) == sorted(list(t))
    
# Add Digits
class Solution(object):
    def addDigits(self, num):
        def convert(val):
            return sum(int(i) for i in str(val))

        while len(str(num)) != 1:
            num = convert(num)

        return num

# Ugly Number
class Solution(object):
    def isUgly(self, num):
        if num <= 0:
            return False
        
        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5
        
        return num == 1