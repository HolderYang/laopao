import re
s = "Alex:1994,Sunny:1996"
pattern = r":"
print(re.split(r":,",s)) #按照正则表达式匹配到的内容切割字符串
print(re.sub(pattern, "-", s)) #用-替换匹配到的字符串，返回替换后的字符串


s = "今年是2019年,建国70周年"
pattern = r"\d+"
#返回迭代器对象
it = re.finditer(pattern, s)
for item in it:
    print(item.group()) #group方法获取match对象所对应的内容

#完全匹配字符串
m = re.fullmatch(r"[,\w]+",s)
print(m.group())
#匹配字符串开始位置
match_start = re.match(r"\w+",s)
print(match_start.group())
#匹配第一处符合正则规则的内容
m = re.search(r"\d+",s)
print(m.group())

#属性方法
regxt = re.compile(r"(ab)cd(?P<pig>ef)")
obj = regxt.match("abcdefjhi")
print(obj.span())
print(obj.groupdict()) #捕获组字典
print(obj.groups()) #子组对应内容的元组
print(obj.group()) #默认返回match对象匹配到的全部内容
print(obj.group(1)) #获取第一个子组内容

print("=============")
str =  'aalii   a bushy shrub,'
word = re.findall(r"([a-zA-Z]+)\b",str)
tup = re.findall(r"(\S+)\s+(.*)",str)
translate = re.findall(r"\b[a-zA-Z]+",str)

print(word)
print(tup)
print(translate)