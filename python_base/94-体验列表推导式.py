# 需求：创建一个0-10的列表。

# while 循环实现
# 1.准备一个空列表
list1 = []

# 2.书写循环，依次追加数字到空列表list1中
i = 0
while i < 10:
    list1.append(i)
    i += 1

print(list1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for循环实现
list1 = []
for i in range(10):
    list1.append(i)

print(list1)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 列表推导式实现
list1 = [i for i in range(10)]
print(list1)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
