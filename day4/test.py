def test1(p):
    v1 = 1
    count = 0
    while v1 < p:
        count = count + 1
        v1 <<= 1
    return count


print(test1(1024))
