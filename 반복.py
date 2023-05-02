#2741번

N = int(input())

for i in range(N):
    i = i + 1
    print(i)

#10872번

n = int(input())

result = 1
if n > 0 :
    for i in range(1, n+1):
        result *= i
print(result)

#10950번

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(A+B)

#10952번

while True :
    A, B = map(int, input().split())
    if A == 0 and B == 0 : break
    else : print(A+B)

#2739번

N = int(input())

for i in range(1, 10):
    print(N, "*", i, "=", N*i)
    i = i + 1

#2438번

N = int(input())

i = 0

for i in range(0, N):
    i = i + 1
    print("*" * i)

#10951번

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break