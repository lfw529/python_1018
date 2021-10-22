name_list = ['TOM', 'Lily', 'ROSE']

# 1. del
# del 直接删除列表

# del name_list
# del(name_list)
# print(name_list)   #报错，已直接删除变量

# del 可以删除指定下标的数据
# del name_list[0]
# print(name_list)    # ['Lily', 'ROSE']

# 2. pop() -- 删除指定下标的数据，如果不指定下标，默认删除最后一个数据，
# 无论是按照下标还是删除最后一个，pop函数都会返回这个被删除的数据
# del_name = name_list.pop()     # ROSE    ||    ['TOM', 'Lily']
# del_name = name_list.pop(1)      # ROSE    ||    ['TOM', 'Lily']
# print(del_name)
# print(name_list)

# 3. remove(数据)
# name_list.remove('ROSE')    # ['TOM', 'Lily']
# print(name_list)

# 4. clear() -- 清空
name_list.clear()    # []
print(name_list)

