from sys import setrecursionlimit
setrecursionlimit(10000) # 보통 재귀 함수 때 (함수 안에 그 함수가 다시 있는 경우) 써주기. 미리 안 써주도라도 recursion 에러 나면 써주면 됨
n = int(input())

grid = [] # 주어지는 2차원 배열 공간을 grid로
cnt = 0  # (생기는 안전한 영역의) 개수 
visited = [[False for i in range(n)] for i in range(n)]  # 방문 여부. 우선 처음에 다 False로 깔아줌
for _ in range(n): # n번만큼 아래 코드를 실행해주겠다는 것
    grid.append(list(map(int, input().split())))  # grid input (2차원 배열). 테스트 시, 한 줄 씩 넣어주는 것



def is_valid(x,y):  # grid 밖으로 넘어가는지 확인!
    if x >= 0 and x < n and y < n and y >= 0:
        return True # 함수의 결과값으로 True 값을 넣겠다는 것
    return False

def dfs(x,y):
    if not is_valid(x,y): #위에서 is_valid의 결과값으로 True 나 False가 들어가겠지~
        return False
    if visited[x][y] == False and grid[x][y] != 0: # 전에 방문하지 않았고! + 안 잠기고 살아남았는지 확인 
        visited[x][y] = True # 이제 방문 했으면 true로 바꿔주는거지 ~
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False


def rain(depth):
    global visited #global은 전역변수화 해주는 것 
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
    rain(depth) #함수 부르는 것
    cnt = 0  # 영역 개수 세는 변수
    for x in range(n):
        for y in range(n):
            if dfs(x,y):
                cnt += 1

    answers.append(cnt)
    depth += 1

print(max(answers))