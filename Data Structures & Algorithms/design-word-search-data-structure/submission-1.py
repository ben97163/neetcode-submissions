class TreeNode:
    def __init__(self, char):
        self.char = char
        self.next = {}

class WordDictionary:

    def __init__(self):
        self.root = TreeNode('#')

    def addWord(self, word: str) -> None:
        cur = self.root
        for i, s in enumerate(word):
            if s not in cur.next:
                cur.next[s] = TreeNode(s)
            cur = cur.next[s]

        cur.next["#"] = None

    def search(self, word: str) -> bool:
        cur = self.root
        def dfs(i, node):
            if i == len(word):
                if node:
                    return '#' in node.next.keys()
                return False
            elif word[i] == '.':
                for s in node.next.keys():
                    if dfs(i+1, node.next[s]):
                        return True
                return False
            elif word[i] not in node.next:
                return False
            else:
                return dfs(i+1, node.next[word[i]])
        
        return dfs(0, self.root)
