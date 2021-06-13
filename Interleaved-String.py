class Solution:
    def solve(self, s0, s1):
        s0 = list(s0)
        s1 = list(s1)
        result = []
        for pair in zip(s0,s1):
            result.extend(pair)
        if len(s0) != len(s1):
            lsts = [s0, s1]
            smallest = min(lsts, key = len)
            biggest = max(lsts, key = len)
            rest = biggest[len(smallest):]
            result.extend(rest)
        return "".join(result)
        