#1330번

A, B = map(int, input().split())

if A > B :
    print(">")
elif A < B:
    print("<")
else :
    print("==")

#9498번

score = int(input())
if score >= 90 : print("A")
elif score >= 80 : print("B")
elif score >= 70 : print("C")
elif score >= 60 : print("D")
else : print("F")

#14681번

x = int(input())
y = int(input())
if x > 0 and y > 0 : print(1)
elif x < 0 and y > 0 : print(2)
elif x < 0 and y < 0 : print(3)
else : print(4)

#2753번

x = int(input())
if ((x % 4 == 0) and (x % 100 != 0)) or (x % 400 == 0) : print(1)
else : print(0)

#2420번

x, y = map(int, input().split())
if x >= y : print(x-y)
else : print(-(x-y))
