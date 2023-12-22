class Node:
    def __init__(self, val: str) -> None:
        self.val = val
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = Node("")

    def addWord(self, word: str) -> None:
        # 1 <= len(word) <= 25
        # Time: O(len(word)) => O(25)
        curNode = self.root
        for c in word:
            if curNode.children.get(c) is None:
                curNode.children[c] = Node(c)
            curNode = curNode.children[c]
        curNode.isWord = True

    def search(self, word: str) -> bool:
        # at most 2 dot
        # Time: O(26**2*len(word)) => O(16900) ~ O(2*10^4)
        def recur(i: int, curNode: Node):
            if i == len(word):
                return curNode.isWord
            if word[i] == '.':
                for c in curNode.children:
                    if recur(i+1, curNode.children[c]):
                        return True
                return False
            if curNode.children.get(word[i]) is None:
                return False
            return recur(i+1, curNode.children[word[i]])
        return recur(0, self.root)


def run(ops, words):
    obj = WordDictionary()
    out = [None]
    for i in range(1, len(ops)):
        word = words[i][0]
        if ops[i] == 'addWord':
            out.append(obj.addWord(word))
        if ops[i] == 'search':
            out.append(obj.search(word))
    print(out)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
ops = ["WordDictionary", "addWord", "addWord", "addWord", "search",
       "search", "search", "search", "search", "search", "addWord", "search"]
words = [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"],
         [".ad"], ["b.."], ["b."], [".."], ["zz"], [".."]]
run(ops, words)
