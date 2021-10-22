# 单引号表示字符串
a = 'hello ' \
    'world'
print(a)
print(type(a))

# 双引号表示字符串
b = "TOM"
print(type(b))

# 三引号 [支持换行]
e = '''i am TOM'''
print(type(e))

f = """I 
am TOM"""
print(type(f))
print(f)

# I'm TOM  用双引号处理包含单引号的字符串
c = "I'm TOM"
print(c)
print(type(c))

# d = 'I'm TOM'  转义符号处理含单引号的字符串
d = 'I\'m TOM'
print(d)
print(type(d))



