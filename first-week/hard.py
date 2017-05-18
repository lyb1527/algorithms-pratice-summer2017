##Target-sum
'''
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.


'''
class Solution(object):

    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s = sum(nums)
        if s < target or (s + target) % 2:
            return 0

        # This is to find number of subsets that have sum equal to target
        sum_of_positives = (s + target) / 2
        dp = [1] + [0] * sum_of_positives
        for num in nums:
            for i in xrange(sum_of_positives, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[-1]
