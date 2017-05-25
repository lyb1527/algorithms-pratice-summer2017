#convert sorted array to binary search tree
'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

#每次二分，递归建立左右子树
'''

class Solution:

    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        left, right = 0, len(nums) - 1
        return self.dfs(nums, left, right)

    def dfs(self, nums, left, right):
        if left == right:
            return TreeNode(nums[left])
        if left > right:
            return None
        mid = (left + right)>>1
        root = TreeNode(nums[mid])
        root.left = self.dfs(nums, left, mid-1)
        root.right = self.dfs(nums, mid+1, right)
        return root


# find the root first, then recursively build each left and right subtree

class Solution:
    # @param num, a list of integers
    # @return a tree node
    # 12:37
    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root



##combintionSum
'''
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]

'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in xrange(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)


##combinationSum-II()
#Each number can obly used once
'''
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
'''
class Solution:

    def combinationSum2(self, candidates, target):
        # Sorting is really helpful, se we can avoid over counting easily
        candidates.sort()
        result = []
        self.combine_sum_2(candidates, 0, [], result, target)
        return result

    def combine_sum_2(self, nums, start, path, result, target):
        # Base case: if the sum of the path satisfies the target, we will consider
        # it as a solution, and stop there
        if not target:
            result.append(path)
            return

        for i in xrange(start, len(nums)):
            # Very important here! We don't use `i > 0` because we always want
            # to count the first element in this recursive step even if it is the same
            # as one before. To avoid overcounting, we just ignore the duplicates
            # after the first element.
            if i > start and nums[i] == nums[i - 1]:
                continue

            # If the current element is bigger than the assigned target, there is
            # no need to keep searching, since all the numbers are positive
            if nums[i] > target:
                break

            # We change the start to `i + 1` because one element only could
            # be used once
            self.combine_sum_2(nums, i + 1, path + [nums[i]],
                               result, target - nums[i])




## combinationSum-III
'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]

'''

 class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        if n > sum([i for i in range(1, 11)]):
            return []

        res = []
        self.sum_help(k, n, 1, [], res)
        return res


    def sum_help(self, k, n, curr, arr, res):
        if len(arr) == k:
            if sum(arr) == n:
                res.append(list(arr))
            return

        if len(arr) > k or curr > 9:
            return

        for i in range(curr, 10):
            arr.append(i)
            self.sum_help(k, n, i + 1, arr, res)
            arr.pop()

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return []

        self.res = []
        self.sol = []
        self.combinationSumRec(k, n, 1)
        return self.res

    def combinationSumRec(self, k, target, st):
        if target < 0:
            return
        if k == 0:
            if target == 0:
                self.res.append(copy.deepcopy(self.sol))
            return

        for i in xrange(st, 10):
            self.sol.append(i)
            self.combinationSumRec(k - 1, target - i, i + 1)
            self.sol.pop()




## combinationSum - IV
'''
Given an integer array with all positive numbers and no duplicates,
find the number of possible combinations that add up to a positive integer target.

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
'''

class Solution(object):
    def combinationSum4(self, nums, target):
        nums, combs = sorted(nums), [1] + [0] * (target)
        for i in range(target + 1):
            for num in nums:
                if num  > i: break
                if num == i: combs[i] += 1
                if num  < i: combs[i] += combs[i - num]
        return combs[target]

# 17 / 17 test cases passed.
# Status: Accepted
# Runtime: 116 ms



#sample 45 ms submission
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return 0
        nums.sort()
        dp = [0] * (target+1)
        dp[0] = 1

        for i in range(1, target+1):
            for num in nums:
                if num > i:
                    break
                dp[i] += dp[i-num]
        return dp[target]
