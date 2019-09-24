n = int(input("Enter n"))
m = int(input("Enter m"))
a = int(input("Enter a"))
p = 1
q = 1
while n > a * p:
    p = p + 1
    break
while m > a * q:
    q = q + 1
    break
print(p * q)
