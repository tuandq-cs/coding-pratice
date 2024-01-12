from typing import List


class Account:
    def __init__(self, name: str) -> None:
        self.name = name
        self.head = self.tail = None


class Node:
    def __init__(self, email: str, root: Account) -> None:
        self.email = email
        self.root = root
        self.next = None


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def dfs(email: str):
            visited[email] = True
            emails = [email]
            for n in adjList[email]:
                if visited.get(n) is None:
                    emails.extend(dfs(n))
            return emails

        adjList = {}
        for acc in accounts:
            if adjList.get(acc[1]) is None:
                adjList[acc[1]] = []
            for i in range(2, len(acc)):
                if adjList.get(acc[i]) is None:
                    adjList[acc[i]] = []
                adjList[acc[i]].append(acc[i-1])
                adjList[acc[i-1]].append(acc[i])
        visited = {}
        ans = []
        for acc in accounts:
            if visited.get(acc[1]) is None:
                ans.append([acc[0]] + sorted(dfs(acc[1])))
        return ans


accounts = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"]
]
out = Solution().accountsMerge(accounts)
print(out)

accounts = [["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"], ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"], ["Ethan", "Ethan5@m.co",
                                                                                                                         "Ethan4@m.co", "Ethan0@m.co"], ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"], ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]
out = Solution().accountsMerge(accounts)
print(out)
