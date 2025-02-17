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

path = Path("write_test.txt")
path.write_text("I like eating ice cream.")
# Exception异常处理
# ZeroDivisionError除0错误
try:
    print(5 / 0)
except ZeroDivisionError:
    print("you can't divide by zero")
# filenotfound文件未找到错误
path = Path("test.txt")
try:
    contents = path.read_text()
except FileNotFoundError:
    print("No such file\n")
else:
    print(contents)
# 不需要报告的错误用pass直接跳过
# Json格式数据
# JavaScript Object Notation
# Json.dumps(xxx)存储xxx数据为json格式
# json.loads(xxx)读取json格式的xxx数据
import json

numbers = [1, 2, 3, 4, 5, 6]
contents = json.dumps(numbers)
path = Path("write_test.txt")
path.write_text(contents)
contents = json.loads(path.read_text())
print(contents)
# 路径是否存在path.exists()
# 代码重构 skip 拆分函数功能到其他函数中
