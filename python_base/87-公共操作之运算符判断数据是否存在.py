str1 = 'abcd'
list1 = [10, 20, 30, 40]
t1 = (100, 200, 300, 400)
dict1 = {'name': 'Python', 'age': 30}

# in 和 not in
# 1. 字符a是否存在
print('a' in str1)       # True
print('a' not in str1)   # False

# 2. 数据10是否存在
print(10 in list1)       # True
print(10 not in list1)   # False

# 3. 100是否存在
print(100 not in t1)     # False
print(100 in t1)         # True

# 4. name是否存在
print('name' in dict1)            # True
print('name' not in dict1)        # False
print('name' in dict1.keys())     # True
print('name' in dict1.values())   # False

