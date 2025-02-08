S = input().strip() # 양쪽 공백 없이 받아오기

alphabets = [-1] * 26

for i in range(len(S)):
    index = ord(S[i]) - ord('a') # a를 기준으로 몇번째 알파벳인지
    if alphabets[index] == -1:
        alphabets[index] = i

print(" ".join(map(str, alphabets)))