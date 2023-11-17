class Solution:
    """
    Author: Maharshi Gor
    Date: 2023-11-16
    """
    def minPairSum(self, nums: List[int]) -> int:
        """
        1877. Minimize Maximum Pair Sum in Array

        The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is
        the largest pair sum in a list of pairs.

        For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair
        sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.

        Given an array nums of even length n, pair up the elements of nums into
        n / 2 pairs such that:

        Each element of nums is in exactly one pair, and
        The maximum pair sum is minimized.
        Return the minimized maximum pair sum after optimally pairing up the
        elements.

        Explanation
        -----------

        As we need to minimize the maximum sum. The problem we are solving is,
        we need to come up with the pairs which have the less overall sum. If we
        add the smallest number to the largest number we can attain that. Thus,
        we simply sort the numbers and find the maximum sum of two simultaneously
        moving pointers i and j. where i starts from the begining and j starts
        from the end.
        """
        nums = sorted(nums)
        n = len(nums)
        max_sum = 0
        for i in range(n//2):
            j = n - i - 1
            max_sum = max(max_sum, nums[i] + nums[j])

        return max_sum