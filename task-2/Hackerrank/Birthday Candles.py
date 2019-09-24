

a = []

age = int(input("Enter the age"))

for i in range(age):
    x = int(input("Enter the heights"))
    a.append(x)
max = a[0]
for i in range(1, age):
    if max < a[i]:
        max = a[i]
s = 0
for i in range(0, age):
    if a[i] == max:
        s = s + 1
print(s)
