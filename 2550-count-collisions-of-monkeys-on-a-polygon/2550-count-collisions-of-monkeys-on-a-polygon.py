class Solution:
    def monkeyMove(self, n: int) -> int:
        # Each monkey can move in the clockwise or counter-clockwise direction,
        # so 2 choices for each of n monkeys.

        # There are 2 ^ n number of ways.
        # If all monkey move in clockwise direction, no collision.
        # If all monkey move in counter-clockwise direction, no collision.
        # All other ways, collision happens.

        # So we need to return (2 ^ n - 2) % mod,
        mod = 10**9 + 7
        return ((pow(2,n,mod)) - 2) % mod