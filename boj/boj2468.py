from sys import setrecursionlimit
setrecursionlimit(10000) # 보통 재귀 함수 때 (함수 안에 그 함수가 다시 있는 경우) 써주기. 미리 안 써주도라도 recursion 에러 나면 써주면 됨
n = int(input())

grid = []
cnt = 0  # 개수 
visited = [[False for i in range(n)] for i in range(n)]  # 방문 여부
for _ in range(n):
    grid.append(list(map(int, input().split())))  # grid input (2차원 배열)



def is_valid(x,y):  # grid 밖으로 넘어가는지 확인!
    if x >= 0 and x < n and y < n and y >= 0:
        return True
    return False

def dfs(x,y):
    if not is_valid(x,y):
        return False
    if visited[x][y] == False and grid[x][y] != 0: # 전에 방문하지 않았고! + 안 잠기고 살아남았는지 확인 
        visited[x][y] = True
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False


def rain(depth):
    global visited
    visited = [[False for i in range(n)] for i in range(n)]  # 초기화!
    for x in range(n):
        for y in range(n):
            if grid[x][y] <= depth:  # 지점 높이 <= depth가 비의 높이 -> 잠길 것 
                grid[x][y] = 0  # 잠긴 지점을 0으로 바꾸기 

min_depth = min(min(grid))  # 가장 낮은 높이
max_depth = max(max(grid))  # 가장 높은 높이
depth = min_depth
answers = [1]  # [depth 0일 때 영역 개수, depth 2일 때 영역 개수, depth 3일 때 영역 개수, ... ,max depth일 때 영역 개수]
 
while (depth <= max_depth):
    rain(depth) 
    cnt = 0  # 영역 개수 세는 변수
    for x in range(n):
        for y in range(n):
            if dfs(x,y):
                cnt += 1

    answers.append(cnt)
    depth += 1

print(max(answers))