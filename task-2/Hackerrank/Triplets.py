

a = []

n = int(input("Enter the length"))
for i in range(n):
    x = int(input("Enter the values of 1st"))
    a.append(x)

b = []

for i in range(n):
    y = int(input("Enter the values of 2nd"))
    b.append(y)

k = 0
m = 0
j = 0
while j < n:
    if a[j] > b[j]:
        k = k + 1
    elif a[j] < b[j]:
        m = m + 1
    j = j + 1
c = [k, m]
print(c)
