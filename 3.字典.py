person={'name':'kobe','age':42,'job':'player'}
for k,v in person.items():
    print(k,'：',v)
#遍历字典  打印 键-值

#生成字典
chars=['a','d','d','a','e','w','q']
char_count={}
for char in chars:
     print(char_count[char])
     if char not in char_count:
         char_count[char]=chars.count(char)#字典添加键值对
print(char_count)
max_value=max(char_count.values())
print(max_value)
a=[k for (k,v) in char_count.items() if v == max_value]#由值来找键
print(a)

person={'name':'kobe','age':42,'job':'player'}
dict1={v:k for  k,v in person.items()}#字典推导式键值反转
print(person)
person2={}
for k,v in person.items():
    person2[v]=k
print(person2)