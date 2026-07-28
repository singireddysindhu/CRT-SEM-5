#26.Remove duplicates From sorted array
from typing import List
from xml.dom.minidom import Element
def removeDuplicates(nums: List[int]) -> int:
    i=0
    for j in range(1,len(nums)):
        if nums[i]!=nums[j]:
            i+=1
            nums[i]=nums[j]
    return i+1
nums=[0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))

#27.Remove Element
def removeElement(nums: List[int], val: int) -> int:
    i=0
    for j in range(len(nums)):
        if nums[j]!=val:
            nums[i]=nums[j]
            i+=1
    return i
nums=[3,2,2,3]
val=3
print(removeElement(nums, val))

#167Two Sum II - Input array is sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
numbers = [2, 7, 11, 15] 
target = 9
solution = Solution()