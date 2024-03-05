class Solution:
    def minSwaps(self, s: str) -> int:
        begin, end = 0, len(s) - 1
        balance = 0
        swaps = 0
        while (begin < end):
            if s[begin] == '[': balance += 1
            if s[begin] == ']' : balance -= 1
            
            if balance < 0:
                # move end pointer until found '['
                while (s[end] == ']'):
                    end -= 1
                # swap begin, end, actually I don't need to swap
                # pretend, I already swapped
                swaps += 1
                balance = 1
                end -= 1

            begin += 1
        return swaps
    
s = "]]][[["
#       ^
#       ^
# balance = 1
# swap = 2
out = Solution().minSwaps(s)
print(out)