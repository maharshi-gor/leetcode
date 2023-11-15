class Solution:
    """
    Author: Maharshi Gor
    Date: 2023-11-14
    """
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> \
    int:
        """
        You are given an array of positive integers arr. Perform some operations
        (possibly none) on arr so that it satisfies these conditions:

        The value of the first element in arr must be 1.
        The absolute difference between any 2 adjacent elements must be less
        than or equal to 1. In other words, abs(arr[i] - arr[i - 1]) <= 1 for
        each i where 1 <= i < arr.length (0-indexed). abs(x) is the absolute
        value of x.
        There are 2 types of operations that you can perform any number of
        times:

        Decrease the value of any element of arr to a smaller positive integer.
        Rearrange the elements of arr to be in any order.
        Return the maximum possible value of an element in arr after performing
        the operations to satisfy the conditions.

        Explanation
        -----------
        Here all we can do is rearrange or decrease. And we need to answer the
        max value after doing all the actions and matching the constrains.

        Thus, the easiest way is to sort them in ascending order by doing that,
        we can ensure the element left on the index will be lesser than the
        current index. Time complexity for that will be O(nlogn).

        Now, simply make the 0 index as 1 and iterate over the sorted array to
        check if their difference is <= 1 or not if not we can't get any value
        to replace as the element is the best possible adjucent number as they
        are sorted. Simply change that number to + 1 of the prev number. O(n)

        return max of the array O(n).

        Final time complexity = O(nlogn)
        """
        arr = sorted(arr)
        arr[0] = 1
        n = len(arr)
        for i in range(1, n):
            if arr[i] > arr[i-1] + 1:
                arr[i] = arr[i-1] + 1
        return max(arr)