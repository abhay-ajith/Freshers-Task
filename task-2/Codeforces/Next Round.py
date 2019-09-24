n = int(input("Enter n"))
k = int(input("Enter k"))
score = []
for i in range(n):
    x = int(input("Enter the score"))
    score.append(x)
m = score[k]
s = 0
for j in range(n):
    if score[j] >= m:
        s = s + 1
print(s)
