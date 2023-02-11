import sys
input = sys.stdin.readline

n = int(input())
square=[]
for i in range(n):
    square.append(list(map(int, input().split())))

visited = [[0]*n for i in range(n)]

def dfs(x, y):
    if x>=n or y>=n:
        return False
    value = square[x][y]

    if visited[x][y] == 0:
        visited[x][y] = 1
        dfs(x+value, y)
        dfs(x, y+value)
        return True

dfs(0,0)
if visited[n-1][n-1] == 1:
    print("HaruHaru")
else:print("Hing")



