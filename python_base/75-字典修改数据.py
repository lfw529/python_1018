dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}
# 修改值
dict1['name'] = 'Lily'
print(dict1)    # {'name': 'Lily', 'age': 20, 'gender': '男'}

# 没有 key 则新增
dict1['id'] = 110
print(dict1)    # {'name': 'Lily', 'age': 20, 'gender': '男', 'id': 110}

