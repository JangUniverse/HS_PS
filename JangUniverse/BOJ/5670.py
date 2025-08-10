import sys
input = sys.stdin.readline
#트라이가 없대 ㅅㅂ

class Trie:
    
    def __init__(self):
        self.root = dict()
    
    def insert(self, s):
        node = self.root
        for c in s:
            if not c in node:
                node[c] = dict()
            node = node[c]
        node['*'] = dict()
    
    def search(self, s):
        node = self.root[s[0]]
        cnt = 1
        for c in s[1:]:
            if len(node) > 1:
                cnt += 1
            node = node[c]
        return cnt
#try를 써야하나
while 1:
    try:
        n = int(input())
        trie = Trie()
        word = [input().rstrip() for _ in range(n)]
        ans = 0
        for i in range(n):
            trie.insert(word[i])
        for j in range(n):
            ans += trie.search(word[j])
        print(f'{(ans/n):0.2f}')
    except:
        break
