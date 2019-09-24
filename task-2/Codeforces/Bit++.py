n = int(input("Enter n"))
x = 0
b = []
for i in range(n):
    a = input("Enter the statement")
    b.append(a)
for j in range(n):
    if b[j] == "++X" or b[j] == "X++":
        x = x + 1
    if b[j] == "--X" or b[j] == "X--":
        x = x - 1
print(x)
