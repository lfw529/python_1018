name_list = ['TOM', 'Lily', 'ROSE']

# 1. 修改指定下标的数据
name_list[0] = 'aaa'
print(name_list)     # ['aaa', 'Lily', 'ROSE']

# 2. 逆序 reverse()
list1 = [1, 3, 2, 5, 4, 6]
list1.reverse()
print(list1)    # [6, 4, 5, 2, 3, 1]

# 3. sort() 排序：升序(默认) 和 降序
list1.sort()
print(list1)   # [1, 2, 3, 4, 5, 6]
# list1.sort(reverse=False)
list1.sort(reverse=True)
print(list1)   # [6, 5, 4, 3, 2, 1]





