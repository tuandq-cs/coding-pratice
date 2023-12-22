class Node:
    def __init__(self, val: str) -> None:
        self.val = val
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = Node("")

    def insert(self, word: str) -> None:
        # 1 <= len(word), len(prefix) <= 2000
        curNode = self.root
        for c in word:
            if curNode.children.get(c) is None:
                curNode.children[c] = Node(c)
            curNode = curNode.children[c]
        curNode.isWord = True

    def search(self, word: str) -> bool:
        curNode = self.root
        for c in word:
            if curNode.children.get(c) is None:
                return False
            curNode = curNode.children[c]
        return curNode.isWord

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        for c in prefix:
            if curNode.children.get(c) is None:
                return False
            curNode = curNode.children[c]
        return True


def run(ops, words):
    out = [None]
    obj = Trie()
    for i in range(1, len(ops)):
        word = words[i][0]
        if ops[i] == "insert":
            out.append(obj.insert(word))
        if ops[i] == "search":
            out.append(obj.search(word))
        if ops[i] == "startsWith":
            out.append(obj.startsWith(word))
    print(out)


ops = ["Trie", "insert", "search", "search",
       "startsWith", "insert", "search", "startsWith"]
words = [[], ["apple"], ["apple"], ["app"],
         ["app"], ["app"], ["app"], ["apple"]]
run(ops, words)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
