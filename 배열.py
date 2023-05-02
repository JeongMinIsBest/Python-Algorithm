#10871번
N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")

#10807번
N = int(input())
A = list(map(int, input().split()))
V = int(input())
count = 0

for i in range(N):
    if A[i] == V:
        count += 1
        
print(count)

#5597번
S = [ i for i in range(1, 31)]
for _ in range(28):
    applied = int(input())
    S.remove(applied)

print(min(S))
print(max(S))

#2798번
N, M = map(int, input().split())
C = map(int, input().split())

M.sort()
print(M)