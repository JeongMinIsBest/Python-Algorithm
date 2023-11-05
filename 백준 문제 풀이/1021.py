from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

P = list(map(int, input().split()))

D = deque([i for i in range(1, N+1)])

count = 0

for i in P:
    while True:
        if D[0] == i:
            D.popleft()
            break

        else:
            if D.index(i) < len(D)/2:
                while D[0] != i:
                    D.append(D.popleft())
                    count += 1
            
            else:
                while D[0] != i:
                    D.appendleft(D.pop())
                    count += 1

print(count)