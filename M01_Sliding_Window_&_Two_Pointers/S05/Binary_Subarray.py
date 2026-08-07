#1493 
from typing import List

def longestSubarray(nums: List[int]) -> int:
        left = 0
        zero_count = 0
        max_len = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            # Shrink the window until we have at most 1 zero
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Window size minus 1 because we MUST delete one element
            max_len = max(max_len, right - left)
            
        return max_len
nums = [1,1,0,1]
print(longestSubarray(nums))
#1004
class Solution:
    def longestOnes( nums: list[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_len = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            # Shrink the window if zero count exceeds k
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Update the maximum valid window size
            max_len = max(max_len, right - left + 1)
            
        return max_len
    a=[1,1,1,0,0,0,1,1,1,1,0]
    k=2
    print(longestOnes(a, k))
#930
class Solution:
    def numSubarraysWithSum( nums: List[int], goal: int) -> int:
        def atMost(k: int) -> int:
            if k < 0:
                return 0
            
            left = 0
            current_sum = 0
            total_subarrays = 0
            
            for right in range(len(nums)):
                current_sum += nums[right]
                
                # Shrink window until sum <= k
                while current_sum > k:
                    current_sum -= nums[left]
                    left += 1
                
                # All subarrays ending at 'right' starting from 'left' to 'right' are valid
                total_subarrays += (right - left + 1)
                
            return total_subarrays

        return atMost(goal) - atMost(goal - 1)
    d = [1,0,1,0,1]
    goal = 2
    print(numSubarraysWithSum(d, goal))
    