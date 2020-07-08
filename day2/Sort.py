def derectSort(a):
    if len(a) == 1:
        return a
    for i in range(1, len(a)):
        while i > 0 and a[i] < a[i-1]:
            a[i], a[i-1] = a[i-1], a[i]
            i = i-1


list = [1, 4, 2, 4, 3, 5, 52, 14, 5, 7, 3, 3, 6]

# derectSort(list)
# print(list)
# 直接插入排序。时间复杂度 O(n^2)空间复杂度 O(1)


def select(arr: [int]):
    if len(arr) == 1:
        return arr
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr


list1 = [1, 4, 2, 4, 3, 5, 52, 14, 5, 7, 3, 3, 6]
select(list1)
print(list1)
# 选择排序，先认为第一个为最小值，然后与剩下的每一个做比较，如果有值比他小则换一下下标记录最小值的位置。然后把当前位置的值与最小值做交换


def bubble(arr: [int]):
    for i in range(1, len(arr)):
        for j in range(len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j + i], arr[j]


list2 = [1, 4, 2, 4, 3, 5, 52, 14, 5, 7, 3, 3, 6]
select(list2)
print(list2)

# 冒泡排序一次比较两个数，如果他们的顺序错误，就把他们交换。对没一对相邻的元素做同样的步骤，除了最后一个
