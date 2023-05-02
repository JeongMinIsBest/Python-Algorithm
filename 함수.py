#15964번

A, B = map(int, input().split())
print((A+B)*(A-B))

#2475번

N = map(int, input().split())

result = 0

for i in N:
   result += i ** 2

print(result%10)