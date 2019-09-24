n = int(input('Enter n :'))
b = []

for i in range(n):
    x = input("Enter the string")
    b.append(x)

for i in range(0, n):
    if len(b[i]) == 4 or len(b[i]) < 4:
        print(b[i])
    elif len(b[i]) > 4:
        c = b[i]
        print(c[0] + str(len(c) - 2) + c[-1])
