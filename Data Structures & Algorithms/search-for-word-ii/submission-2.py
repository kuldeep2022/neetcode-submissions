class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def add(self,w):
        cur = self
        for c in w:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.add(w)
        
        ROWS, COLS = len(board), len(board[0])
        res = set()
        visit = set()

        def dfs(r,c,word,node):
            if (r not in range(ROWS) or c not in range(COLS) or (r,c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            
            if node.isWord:
                res.add(word)
            
            dfs(r-1,c,word,node)
            dfs(r+1,c,word,node)
            dfs(r,c-1,word,node)
            dfs(r,c+1,word,node)

            visit.remove((r,c))
        
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,'',root)
       
        return list(res)

        