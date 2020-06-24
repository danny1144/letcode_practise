def derectSort(a):
    if len(a) == 1:
        return a
    for i in range(1, len(a)):
        while i > 0 and a[i] < a[i-1]:
            a[i], a[i-1] = a[i-1], a[i]
            i = i-1


list = [1, 4, 2, 4, 3, 5, 52, 14, 5, 7, 3, 3, 6]

derectSort(list)
print(list)
# 直接插入排序。时间复杂度 O(n^2)空间复杂度 O(1)
