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


def test_get_formatted_name():  # test 代码要以test开头,文件名也是要以test开头:
    formated_name = get_formatted_name("jack", "bill")
    assert formated_name == "Jack Bill"  # assert 为'断言'即是否满足特定条件
    # 运行方法,使用pytest 环境运行程序
