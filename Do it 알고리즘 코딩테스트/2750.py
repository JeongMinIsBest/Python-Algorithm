num = int(input())
N = []


for _ in range(num):
    N.append(int(input()))

N.sort() # 괄호 빼먹지 말기!

for i in range(num):
    print(N[i])