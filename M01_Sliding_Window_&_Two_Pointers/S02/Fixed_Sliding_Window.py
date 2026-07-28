'''
#643. Maximum Average Subarray 1 (Traditional Approach)
from typing import List
def findMaxAverage(nums: List[int], k: int) -> float:
    max_sum=float("-inf")
    n=len(nums)
    for i in range(0,n-k+1):
        sub_sum=0
        for j in range(i,i+k):
            sub_sum+=nums[j]
        max_sum=max(max_sum,sub_sum)
    return max_sum/k

nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums,k))

#using sliding window technique
def findMaxAverage(nums: List[int], k: int) -> float:
    max_sum=sum(nums[0:k])
    n=len(nums)
    for i in range(n-k):
        next_sum=max_sum-nums[i]+nums[i+k]
        max_sum=max(max_sum,next_sum)
    return max_sum/k

nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums,k))
'''
'''
#1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold(sliding Window Approach)
from typing import List
def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    count=0
    n=len(arr)
    window_sum=sum(arr[0:k])
    if window_sum/k>=threshold:
        count+=1
    for i in range(n-k):
        window_sum=window_sum-arr[i]+arr[i+k]
        if window_sum/k>=threshold:
            count+=1
    return count

arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
print(numOfSubarrays(arr,k,threshold))
'''
'''
#1456. Maximum Number of Vowels in a Substring of Given Length(sliding Window Approach)
from typing import List
def maxVowels(s: str, k: int) -> int:
    vowels = set('aeiou')
    count = 0
    n = len(s)
    for i in range(k):
        if s[i] in vowels:
            count += 1
    max_count = count
    for i in range(n - k):
        if s[i] in vowels:
            count -= 1
        if s[i + k] in vowels:
            count += 1
        max_count = max(max_count, count)
    return max_count
s = "abciiidef"
k = 3
print(maxVowels(s,k))
'''