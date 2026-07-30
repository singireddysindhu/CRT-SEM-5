#209. Minimum Size Subarray Sum
from typing import List
def minSubArrayLen(target: int, nums: List[int]) -> int:
    n = len(nums)
    left = 0
    total = 0
    min_length = float('inf')
    for right in range(n):
        total += nums[right]
        while total >= target:
            min_length = min(min_length, right - left + 1)
            total -= nums[left]
            left += 1
    return min_length if min_length != float('inf') else 0
target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target, nums))  

#713. Subarray Product Less Than K
def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0
    left = 0
    product = 1
    count = 0
    for right in range(len(nums)):
        product *= nums[right]
        while product >= k:
            product /= nums[left]
            left += 1
        count += right - left + 1
    return count
nums = [10, 5, 2, 6]
k = 100
print(numSubarrayProductLessThanK(nums, k))

#904. Fruit Into Baskets
def totalFruit(fruits: List[int]) -> int:
    left = 0
    max_length = 0
    fruit_count = {}
    for right in range(len(fruits)):
        fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1
        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length

fruits = [1, 2, 1]
print(totalFruit(fruits))
