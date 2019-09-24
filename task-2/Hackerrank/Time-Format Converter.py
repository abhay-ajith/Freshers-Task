time = input("Enter the time")
m = time[-2:]
twm = time[:-2]
h = int(time[:2])
if m == "AM":
    h = (h + 1) % 12 + 1
    print("%02d" % h) + twm[2:]
elif m == "PM":
    h = h % 12 + 12
    print(str(h) + twm[2:])
