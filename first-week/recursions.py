# recursion/DFS problems
'''
1. combination sum

2. combination sum II

3. N-Queens

4. N-Queens II

5. combinations

6. subsets

7. Word Search

8. Subsets II

9. Number of Islands

10.Combination Sum iii

11. Different ways to Add Parentheses

12. Expression Add Operators


'''


#1. combintion sum
'''
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.
Note:
All numbers (including target) will be positive integers.

The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]

find all subsets that sum to a target, elements can be used mulritple times

# GIST:  sort, then use DFS to iterate
'''

class Solution:
    def combintionSum(self, nums, target):
        nums.sort()
        self.ans = []
        self.res = []

        self.search(0, 0, target, nums)
        return self.ans

    def search(self, cur, sum, target, nums):
        if sum==target:
            self.ans.append(self.res[:])
            return

        n = len(nums)
        while cur < n:
            if sum + nums[cur] <= target:
                self.res.append(nums[cur])
                self.search(cur, sum + nums[cur], target, nums)
                self.res.pop()
            cur += 1



# Combinations
'''
Given two integers n and k, return all possible combinations of k numbers out
of 1 ... n. For example, If n = 4 and k = 2, a solution is: [ [2,4], [3,4], [2,3], [1,2], [1,3], [1,4], ]
'''


class Solution:
    def combinations(self, n, k):
        self.res = []
        tmp = []
        self.dfs(n, k, 1, 0, tmp)
        return self.res

    def dfs(self, n, k, m, p, tmp):
        if k == p:
            self.res.append(tmp[:])
            return
        for i in range(m, n+1):
            tmp.append(i)
            self.dfs(n, k, i+1, p+1, tmp)
            tmp.pop()



a = Solution()
#print(a.combinations(4, 2))









#subsets
class Solution():
    # param nums, a list of integers
    # return a list of list of integers

    def subsets(self, nums):
        nums.sort()
        ans = []
        res = []
        self.search(0, len(nums), nums, res, ans)
        return ans


    def search(self, cur, n, nums, res, ans):
        ans.append(res[:])
        #print('1st')
        #print(ans)
        for i in range(cur, n):
            res.append(nums[i])
            self.search(i+1, len(nums), nums, res, ans)
            res.pop()


class Solution1:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        if nums is None:
            return []

        result = []
        nums.sort()
        self.dfs(nums, 0, [], result)
        return result

    def dfs(self, nums, pos, list_temp, ret):
        # append new object with []
        ret.append([] + list_temp)

        for i in xrange(pos, len(nums)):
            list_temp.append(nums[i])
            self.dfs(nums, i + 1, list_temp, ret)
            list_temp.pop()


a = Solution1()
alist = [1, 2, 3]
print(a.subsets(alist))
