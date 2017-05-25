'''
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
'''


'''
Time complexity: O(N^2), memory: O(1)

The naive approach would be to run a iteration for each element and see whether a duplicate value can be found: this results in O(N^2) time complexity.

public boolean containsDuplicate(int[] nums) {

        for(int i = 0; i < nums.length; i++) {
            for(int j = i + 1; j < nums.length; j++) {
                if(nums[i] == nums[j]) {
                    return true;
                }
            }
        }
        return false;
    }
Time complexity: O(N lg N), memory: O(1) - not counting the memory used by sort

Since it is trivial task to find duplicates in sorted array, we can sort it as the first step of the algorithm and then search for consecutive duplicates.

    public boolean containsDuplicate(int[] nums) {

        Arrays.sort(nums);
        for(int ind = 1; ind < nums.length; ind++) {
            if(nums[ind] == nums[ind - 1]) {
                return true;
            }
        }
        return false;
    }
Time complexity: O(N), memory: O(N)

Finally we can used a well known data structure hash table that will help us to identify whether an element has been previously encountered in the array.

public boolean containsDuplicate(int[] nums) {

    final Set<Integer> distinct = new HashSet<Integer>();
    for(int num : nums) {
        if(distinct.contains(num)) {
            return true;
        }
        distinct.add(num);
    }
    return false;
}
This is trivial but quite nice example of space-time tradeoff.


'''


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        vis = set()
        for num in nums:
            if num in vis:
                return True
            vis.add(num)
        return False


# one line version
class Solution(object):
    def containsDuplicate(self, nums):

        return len(nums) != len(set(nums))


#####containsDuplicate-ii#####

'''
Given an array of integers and an integer k, find out whether there are two
distinct indices i and j in the array such that nums[i] = nums[j] and the
absolute difference between i and j is at most k.

'''


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        for i, v in enumerate(nums):
            if v in dict and i - dict[v] <= k:
                return True
            dict[v] = i
        return False

# java solution

public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet<Integer>();
        for(int i = 0; i < nums.length; i++){
            if(i > k) set.remove(nums[i-k-1]);
            if(!set.add(nums[i])) return true;
        }
        return false;
 }





#####containsNearbyDuplicate-iii#####

'''
Given an array of integers, find out whether there are two distinct indices i
and j in the array such that the difference between nums[i] andnums[j] is at
most t and the difference between i and j is at most k.


'''


'''
思想是分成t+1个桶，对于一个数，将其分到第num / (t + 1) 个桶中，我们只需要查找相同的和相邻的桶的
元素就可以判断有无重复。
比如t = 4，那么0~4为桶0，5~9为桶1，10~14为桶2  然后你懂的- –

'''

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        if t < 0: return False
        div = t + 1
        vis = {}
        for i, num in enumerate(nums):
            index = num / div
            if index in vis \
                    or index - 1 in vis and abs(vis[index - 1] - num) <= t \
                    or index + 1 in vis and abs(vis[index + 1] - num) <= t:
                return True
            vis[index] = num
            if i >= k: del vis[nums[i - k] / div]
        return False




#####Happy-Number#####
'''
A happy number is a number defined by the following process: Starting with any
 positive integer, replace the number by the sum of the squares of its digits,
 and repeat the process until the number equals 1 (where it will stay), or it
 loops endlessly in a cycle which does not include 1. Those numbers for which
 this process ends in 1 are happy numbers.
'''


class Solution():
    def isHappy(self, n):
        table = set()
        while True:
            square_sum = sum(int(i) for i in str(n))
            if square_sum == 1:
                return True
            elif square_sum in table:
                return Flase
            table.add(square_sum)
            n = square_sum



#####single-number#####

'''
Given an array of integers, every element appears twice except for one.
Find that single one.

Your algorithm should have a linear runtime complexity. Could you implement it
without using extra memory?
'''

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ans = 0
        for num in A:
            ans ^=num
        return ans




class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        if not nums:
            return 0

        newTail = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]

        return newTail + 1


a  = Solution()
nums = [1, 2, 2,  3, 4, 4,  5,]
print(a.removeDuplicates(nums))



## subsets Three solutions
# DFS recursively
def subsets1(self, nums):
    res = []
    self.dfs(sorted(nums), 0, [], res)
    return res

def dfs(self, nums, index, path, res):
    res.append(path)
    for i in xrange(index, len(nums)):
        self.dfs(nums, i+1, path+[nums[i]], res)

# Bit Manipulation
def subsets2(self, nums):
    res = []
    nums.sort()
    for i in xrange(1<<len(nums)):
        tmp = []
        for j in xrange(len(nums)):
            if i & 1 << j:  # if i >> j & 1:
                tmp.append(nums[j])
        res.append(tmp)
    return res

# Iteratively
def subsets(self, nums):
    res = [[]]
    for num in sorted(nums):
        res += [item+[num] for item in res]
    return res
