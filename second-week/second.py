#github
## sum of two integers

# two sum
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        dictionary = {}
        for ind, number in enumerate(nums):
            if target - number in dictionary:
                return [dictionary[target-number], ind]
            dictionary[number] = ind
        return False



## Intersection of two linked list
'''
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

＃analysis： https://leetcode.com/articles/intersection-two-linked-lists/

Approach #3 (Two Pointers) [Accepted]

Maintain two pointers pA and pB initialized at the head of A and B, respectively.
 Then let them both traverse through the lists, one node at a time.
When pA reaches the end of a list, then redirect it to the head of B (yes, B,
that's right.); similarly when pB reaches the end of a list, redirect it the head of A.
If at any point pA meets pB, then pA/pB is the intersection node.
To see why the above trick would work, consider the following two lists:
A = {1,3,5,7,9,11} and B = {2,4,9,11}, which are intersected at node '9'.
Since B.length (=4) < A.length (=6), pB would reach the end of the merged list
first, because pB traverses exactly 2 nodes less than pA does. By redirecting
pB to head A, and pA to head B, we now ask pB to travel exactly 2 more nodes
than pA would. So in the second iteration, they are guaranteed to reach the
intersection node at the same time.
If two lists have intersection, then their last nodes must be the same one.
So when pA/pB reaches the end of a list, record the last element of A/B respectively. If the two last elements are not the same one, then the two lists have no intersections.

'''
#345ms, two pointers
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1=headA
        p2=headB
        len1=0
        len2=0
        while p1:
            len1+=1
            p1=p1.next
        while p2:
            len2+=1
            p2=p2.next
        if len1>len2:
            diff=len1-len2
            while diff>0:
                headA=headA.next
                diff-=1
        else :
            diff=len2-len1
            while diff>0:
                headB=headB.next
                diff-=1
        while headA:
            if headA==headB:
                return headA
            else:
                headA=headA.next
                headB=headB.next

#435ms hash table solution
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        Aptr = headA
        A = set()
        while Aptr:
            A.add(Aptr)
            Aptr = Aptr.next

        Bptr = headB
        while Bptr:
            if Bptr in A:
                return Bptr
            Bptr = Bptr.next

        return None


##Intersection of two arrays
'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
'''

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))



class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        map = {}
        for i in nums1:
            map[i] = map[i]+1 if i in map else 1
        for j in nums2:
            if j in map and map[j] > 0:
                res.append(j)
                map[j] = 0
        return res



##Intersection of two arrays-II
'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

'''

#sample 39 ms submission
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict = {}
        res = []
        for num in nums1:
            dict[num] = dict.get(num, 0) + 1
        for num in nums2:
            if num in dict and dict[num] > 0:
                dict[num] -= 1
                res.append(num)
        return res


from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        counter = Counter(nums1)

        for num in nums2:
            if counter[num]>0:
                res.append(num)
                counter[num]-=1
        return res

## reverse-bits
'''

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
'''


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        # 对于这道题，我们只需要把要翻转的数从右向左一位位的取出来，
        # 然后加到新生成的数的最低位即可

        ans = 0
        for i in range(32):
            ans <<= 1
            ans |= (n & 1)
            n >>=1
        return ans


## reverse integer
'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
'''


## valid Parentheses
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid
 but "(]" and "([)]" are not.
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        dic = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in dic.values():
                stack.append(ch)
            elif not stack or stack.pop() != dic[ch]:
                return False

        return stack == []


#sample 39 ms submission
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        for i in s:
            if i=='(':
                stack.append(')')
            elif i =='{':
                stack.append('}')
            elif i =='[':
                stack.append(']')
            elif len(stack) ==0 or i !=stack.pop():
                return False
        if len(stack)==0:
            return True
        else:
            return False



##search insert position
'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ### find the first position >= target###
        if not nums or len(nums) == 0:
            return 0
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] >= target:
            return start
        elif nums[end] >= target:
            return end
        else:
            return end + 1




## Valid perfect square
'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False

'''
#sample 32 ms submission
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        r = num
        while r*r > num:
            r = (r + num/r) / 2
        return r*r == num

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start=1
        end=num
        while start<=end:
            mid=(start+end)/2
            if mid**2<num:
                start=mid+1
            elif mid**2>num:
                end=mid-1
            else:
                return True
        return False


## Longest increasing subsequences
'''

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

#analysis: https://leetcode.com/articles/longest-increasing-subsequence/
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) / 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size


#sample 46 ms submission
#DP with binary search

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=[]
        for x in range(len(nums)):
            # print 'x=', x
            low=0
            high=len(ans)-1

            while low <= high:
                mid=(low+high)/2
                # print "mid = ", mid , low, high
                if ans[mid]<nums[x]:
                    low=mid+1
                else:
                    high=mid-1

            if low >= len(ans):
                ans.append(nums[x])
            else:
                ans[low]=nums[x]
            # print 'ans=', ans
            # print ''

        return len(ans)

## heaters




## russian doll envolopes
'''

You have a number of envelopes with widths and heights given as a pair of
integers (w, h). One envelope can fit into another if and only if both the width
 and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes
you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
'''
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if len(envelopes) == 0: return 0
        senv = sorted(envelopes, key=lambda (w, h):(w, -h))
        seq = [senv[0][1]]
        for r in senv[1:]:
            if r[1] > seq[-1]:
                seq.append(r[1])
            else:
                li = bisect.bisect_left(seq, r[1])
                seq[li] = r[1]

        return len(seq)



## search for a range

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums) == 0:
            return [-1, -1]

        start, end = 0, len(nums)-1
        while start+1 < end:
            mid = start + (end-start)/2
            if nums[mid] == target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            leftBound = start
        elif nums[end] == target:
            leftBound = end
        else:
            return [-1, -1]


        start, end = 0, len(nums)-1
        while start+1 < end:
            mid = start + (end-start)/2
            if nums[mid] == target:
                start = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[end] == target:
            rightBound = end
        elif nums[start] == target:
            rightBound = start

        return [leftBound, rightBound]




## find peak elements
class Solution(object):
    def findPeak(self, A):
        start, end = 1, len(A) - 2
        while start + 1 <  end:
            mid = (start + end) / 2
            if A[mid] < A[mid - 1]:
                end = mid
            elif A[mid] < A[mid + 1]:
                start = mid
            else:
                end = mid

        if A[start] < A[end]:
            return end
        else:
            return start


## split array largest sum
'''
Given an array which consists of non-negative integers and an integer m,
you can split the array into m non-empty continuous subarrays. Write an
algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

'''




##Max Sum of Rectangle No Larger Than K
