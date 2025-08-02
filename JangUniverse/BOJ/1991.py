import sys
input = sys.stdin.readline

def preorder(x):
    if x != '.':
        print(x, end='')
        preorder(tree[x][0])
        preorder(tree[x][1])

def inorder(x):
    if x != '.':
        inorder(tree[x][0])
        print(x, end ='')
        inorder(tree[x][1])
    
def postorder(x):
    if x != '.':
        postorder(tree[x][0])
        postorder(tree[x][1])
        print(x, end ='')

n = int(input())
tree = dict()

for i in range(n):
    root, lnode, rnode = input().split()
    tree[root] = [lnode, rnode]
    
preorder('A')
print()
inorder('A')
print()
postorder('A')