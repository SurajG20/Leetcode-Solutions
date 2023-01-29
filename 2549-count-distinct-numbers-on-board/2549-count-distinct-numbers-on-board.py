class Solution:
    def distinctIntegers(self, n: int) -> int:
        #"for 10^9 days", it's quite a long duration.
        # And n is much smaller than the number of days.

        # It's a brain-teaser,
        # the duration is long enough to generate all cards.
        if n == 1:
            return 1
        else:
            return n - 1
        