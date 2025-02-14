# Chapter 7
message = input("Input something:")
print(message)
# 多行输出
prompt = "Hi what's your name"
prompt += "\nAnd how are you?"
print(prompt)
# int()强制类型转换,而不是input()的字符串
prompt = input("age: ")
prompt = int(prompt)
if prompt >= 18:
    print("Damn! You are adult!")
# % 求模运算符 same as C
