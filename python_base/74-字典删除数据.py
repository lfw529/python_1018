dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}

# del 删除字典或指定的键值对
# del(dict1)
# print(dict1)      # 报错，已经不存在

# del dict1['name']
# del dict1['names']  # 报错
# print(dict1)

# clear()      清空
dict1.clear()
print(dict1)    # {}
