# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

a = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100]
number = 7

for i in range(len(a)):
    if number < a[i]:
        a.insert(i, number)
        break
print(a)
