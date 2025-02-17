# Chapter 9: File
from pathlib import Path

path = Path("test.txt")
contents = path.read_text()  # read_text会在到达文件末尾时返回一个空字符串
print(contents)
contents = contents.rstrip()
print(contents)  # 这样就删除了额外的空行

# 分割内容
string_num = len(contents)
print(string_num)
print(repr(contents))
contents = contents.splitlines()
string_len = ""
for line in contents:
    string_len += line
string_num = len(string_len)
print(string_num)
print(repr(string_len))  # 可以看出,分割后换行符就消失了,不计入字符数
