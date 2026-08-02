class TreeNode:
    def __init__(self, char):
        self.char = char
        self.next = {}

class PrefixTree:
    def __init__(self):
        self.root = TreeNode("#")

    def insert(self, word: str) -> None:
        cur = self.root
        for i, s in enumerate(word):
            if s not in cur.next:
                cur.next[s] = TreeNode(s)
            cur = cur.next[s]

        cur.next["#"] = None

    def search(self, word: str) -> bool:
        cur = self.root
        for s in word:
            if s not in cur.next:
                return False
            cur = cur.next[s]
        
        if '#' in cur.next.keys():
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for s in prefix:
            if s not in cur.next:
                return False
            cur = cur.next[s]
    
        return True
        