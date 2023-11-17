class Solution:
    """
    Author: Maharshi Gor
    Date: 2023-11-16
    """
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        1980. Find Unique Binary String

        Given an array of strings nums containing n unique binary strings each
        of length n, return a binary string of length n that does not appear in
        nums. If there are multiple answers, you may return any of them.

        Explanation
        -----------

        Here, we have list of all the patterns of binary string of fixed size.
        Now, we want to identify whether the unique combination we come up with
        is present in the input list.

        This it self indicates you need to use a set to retrive your data in
        O(1) time. Once done we write a recursive function which will take in
        current string and the index which we are changing.

        We will pass it fixed length all zero string. The recursive function is
        essentially doing the DFS for us, as if get to the left most node
        (string with all 0's) and start manuplating each bit and check different
        combinations.

        It is effective as we just want to find one of the not present string.
        """
        bs = set(nums)

        def find_unique_bs(current_bs, i):
            if current_bs not in bs:
                return current_bs

            if i == len(current_bs):
                return None

            l_search = find_unique_bs(current_bs, i+1)

            if l_search is not None:
                return l_search

            current_bs = list(current_bs)
            current_bs[i] = '1'

            r_search = find_unique_bs(''.join(current_bs), i+1)

            return r_search

        return find_unique_bs(''.join(['0' for i in range(len(nums[0]))]), 0)
