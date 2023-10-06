class Solution:
    def integerBreak(self, n: int) -> int:
        """
        Given an integer n, break it into the sum of k positive integers,
        where k >= 2, and maximize the product of those integers.

        Return the maximum product you can get.

        Explanation
        -----------
        Here we are trying to find the optimal number (x) which has
        z = x^exponent * y value highest and (x * exponent) + y = n.

        To find that value of x and y we divid the value n from 1 to mid and get
        the value of exponent. we will use the fraction of this division if it
        greater than or equal to 0.5 we will use direct integer value of the
        division. If not we will take one minus.

        The idea here is to get:

        n = 10
        we need 3 + 3 + 4
        Thus we need
        x = 3
        exponent = 2
        y = 4

        n = 8
        we need 3 + 3 + 2
        Thus we need
        x = 3
        exponent = 2
        y = 2
        """

        # Checking the base condition for 2
        if n == 2:
            return 1

        # Initialize base value
        max_value = 1

        # Use mid value as the breaking needs atleast two component
        mid = (n // 2) + 1

        for x in range(1, mid + 1):

            # Figure out we need to
            if (n / x) - (n // x) >= 0.5:
                exponent = (n // x)
            else:
                exponent = (n // x) - 1
            y = n - (x * exponent)
            z = pow(x, exponent) * y
            max_value = max(z, max_value)
        return max_value