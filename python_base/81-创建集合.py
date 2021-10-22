# 1. 创建有数据的集合
s1 = {10, 20, 30, 40, 50}
print(s1)  # {40, 10, 50, 20, 30}

s2 = {10, 30, 20, 40, 30, 20}
print(s2)  # {40, 10, 20, 30}

s3 = set('abcdefg')
print(s3)   # {'e', 'f', 'g', 'b', 'c', 'd', 'a'}

# 2. 创建空集合: set()
s4 = set()
print(s4)   # set()
print(type(s4))   # <class 'set'>

s5 = {}
print(type(s5))   # <class 'dict'>

