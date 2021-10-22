list1 = [10, 20, 30, 20, 40, 50]
s1 = {100, 300, 200, 500}
t1 = ('a', 'b', 'c', 'd', 'e')

# tuple(): 转换成元组
print(tuple(list1))    #   (10, 20, 30, 20, 40, 50)
print(tuple(s1))       #   (200, 100, 500, 300)

# list()：转换成列表
print(list(s1))        # [200, 100, 500, 300]
print(list(t1))        # ['a', 'b', 'c', 'd', 'e']

# set()：转换成集合
print(set(list1))      # {40, 10, 50, 20, 30}
print(set(t1))         # {'a', 'd', 'c', 'b', 'e'}




