# Chapter 11: Test Code
# 2025-02-18
# 使用pytest测试代码
def get_formatted_name(first, last):
    fullname = f"{first} {last}"
    return fullname.title()


print("Enter 'q' to quit!")
while True:
    first = input("Enter the first name:")
    if first == "q":
        break
    last = input("Enter the last name:")
    if first == "q":
        break

    formated_name = get_formatted_name(first, last)
    print("Formated name is:", formated_name)
# 单元测试unit test 全覆盖测试full coverage
# test_pytest_check中为对单一函数的测试,也可以有多个函数
# 接下来是对于类的测试,在survey文件中
