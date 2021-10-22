name_list = ['TOM', 'Lily', 'ROSE']

# 单个数据
name_list.extend('xiaoming')
print(name_list)      # ['TOM', 'Lily', 'ROSE', 'x', 'i', 'a', 'o', 'm', 'i', 'n', 'g']

# 序列数据
name_list.extend(['xiaoming', 'xiaohong'])

print(name_list)  # ['TOM', 'Lily', 'ROSE', 'x', 'i', 'a', 'o', 'm', 'i', 'n', 'g', 'xiaoming', 'xiaohong']

# extend() 追加数据是一个序列，把数据序列里面的数据拆开然后逐一追加到列表的结尾