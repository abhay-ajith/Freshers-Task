R = int(input("Enter the number of rows:"))

matrix = []
print("Enter the entries rows:")

for i in range(R):
    a = []
    for j in range(R):
        a.append(int(input()))
    matrix.append(a)
d1 = 0
q = 0
while q < R:
    d1 = d1 + matrix[q][q]
    q = q + 1
w = 0
e = 2
d2 = 0
while w < R:
    if w + e == 2:
        d2 = d2 + matrix[w][e]
        w = w + 1
        e = e - 1
print(d1)
print(d2)
print(abs(d1 - d2))
