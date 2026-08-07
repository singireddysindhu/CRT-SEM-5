#1480

def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums

nums = [1,2,3,4]
print(runningSum(nums))
#1732
from typing import List
def largestAltitude(gain: List[int]) -> int:
    max_altitude = 0
    current_altitude = 0

    for g in gain:
        current_altitude += g
        max_altitude = max(max_altitude, current_altitude)
        
        return max_altitude
a=[-5,1,5,0,-7]
print(largestAltitude(a))
#1991
def findMiddleIndex(nums: List[int]) -> int:
    total_sum = sum(nums)
    left_sum = 0

    for i, num in enumerate(nums):
        # right_sum is the remaining total minus left_sum and current number
            right_sum = total_sum - left_sum - num
            
            if left_sum == right_sum:
                return i
                
            left_sum += num
            
    return -1
a=[2,3,-1,8,4]
print(findMiddleIndex(a))
#724
def pivotIndex(nums: List[int]) -> int:
    total_sum = sum(nums)
    left_sum = 0

    for i, num in enumerate(nums):
        # right_sum is the remaining total minus left_sum and current number
        right_sum = total_sum - left_sum - num
        
        if left_sum == right_sum:
            return i
            
        left_sum += num
        
    return -1
a=[1,7,3,6,5,6]
print(pivotIndex(a))
#523
class Solution:
    def checkSubarraySum(nums: List[int], k: int) -> bool:
        # Map stores {remainder: first_seen_index}
        # {0: -1} handles the case where a valid subarray starts at index 0
        remainder_map = {0: -1}
        running_sum = 0

        for i, num in enumerate(nums):
            running_sum += num
            remainder = running_sum % k

            if remainder in remainder_map:
                # Check if subarray length is at least 2
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                # Store only the FIRST time a remainder is seen to keep maximum distance
                remainder_map[remainder] = i

        return False