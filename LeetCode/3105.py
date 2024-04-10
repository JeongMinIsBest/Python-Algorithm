class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        n = len(nums)                        # get the length
        longest_length = 1
        increasing_length = 1
        decreasing_length = 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                increasing_length += 1
                decreasing_length = 1
            elif nums[i] < nums[i - 1]:
                decreasing_length += 1
                increasing_length = 1
            else:
                increasing_length = 1
                decreasing_length = 1

            longest_length = max(longest_length, increasing_length, decreasing_length)

        return longest_length

        # we have to find the subarrays, which is gradually increasing or decreasing
        # solution : to check the count
        # when the wrong or weird number comes out, we have to set again