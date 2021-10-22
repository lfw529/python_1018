mystr = "hello world and itcast and itheima and Python"

# 1. replace() 把and换成he  #** 说明replace函数有返回值，返回值是修改后的字符串
# new_str = mystr.replace('and', 'he')  # hello world he itcast he itheima he Python
# new_str = mystr.replace('and', 'he', 1)  # hello world he itcast and itheima and Python

# 替换次数如果超出子串出现的次数，表示替换所有这个子串
new_str = mystr.replace('and', 'he', 10)  # hello world he itcast he itheima he Python
# # print(mystr)
print(new_str)

# ***** 调用了replace函数后，发现原有字符串的数据并没有做到修改，修改后的数据是replace函数的返回值
# --- 说明 字符串是不可变数据类型
# 数据是否可以改变划分为 可变类型 和 不可变类型

# 2. split() -- 分割，返回一个列表, 丢失分割字符
# list1 = mystr.split('and')     # ['hello world ', ' itcast ', ' itheima ', ' Python']
list1 = mystr.split('and', 2)    # ['hello world ', ' itcast ', ' itheima and Python']
print(list1)


# 3. join() -- 合并列表里面的字符串数据为一个大字符串
mylist = ['aa', 'bb', 'cc']
new_str = '...'.join(mylist)  # aa...bb...cc
print(new_str)
