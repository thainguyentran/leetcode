
"""Given an array, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

from typing import List


class Solution:

    def reverseArray(self, left, right, array):
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead."""

        k %= len(nums)  # If k > N : exact how many rotation
        self.reverseArray(0, len(nums) - 1, nums)  # Reverse from 0 to n
        self.reverseArray(0, k - 1, nums)  # Reverse from 0 to K-1
        self.reverseArray(k, len(nums) - 1, nums)  # Reverse from K to N-1

nums = [1, 2, 3, 4, 5, 6, 7]
k: int = 3
p = Solution()
p.rotate(nums, k)
print(nums)
