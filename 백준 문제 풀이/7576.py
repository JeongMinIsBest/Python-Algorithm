from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())


tomato = [list(map(int, sys.stdin.readline().split())) for i in range(M)] # 세로만큼 토마토 값을 받아오기

# 범위 파악
# 데이터 받는 배열 + 거리 계산 배열 + 방문 배열

queue = deque([])

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 왼 / 오 / 위 / 아래 순서대로

answer = 0

for i in range(M):
    for j in range(N):
        if tomato[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft() # 토마토 먼저 좌표 꺼내기

        for i in range(4):
            Nx, Ny = dx[i] + x, dy[i] + y #여러 방면으로 움직이면서 익힐 토마토를 찾기
            if 0 <= Nx < N and 0 <= Ny < M and tomato[Nx][Ny] == 0 :
                tomato[Nx][Ny] = tomato[x][y] + 1
                queue.append([Nx, Ny])

bfs()

for i in tomato:
    for j in i:
        if j == 0: #토마토를 익히지 못했다면
            print(-1)
            exit(0)
        answer = max(answer, max(i))

print(answer -1)


