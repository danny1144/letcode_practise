
def print1():
    for a in range(0, 1001):
        for b in range(0, 1001):
            c = 1000-1-b
            if a+b+c == 1000 and a**2+b**2 == c**2:
                print(a, b, c)


print1()
