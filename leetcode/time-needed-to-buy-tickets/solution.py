from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        numTickets = tickets[k]
        # how many time to buy numTickets - 1
        time = 0
        for i in range(n):
            time += min(tickets[i], numTickets - 1)
            tickets[i] = max(tickets[i] - numTickets + 1, 0)
        # at this time, the person at position k need to buy only 1 ticket to finish
        # so he need to wait these front people has tickets[i] > 0
        for i in range(k+1):
            time += min(1, tickets[i])
        return time