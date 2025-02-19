from TestCode import get_formatted_name


def test_get_formatted_name():  # test 代码要以test开头
    formated_name = get_formatted_name("jack", "bill")
    assert formated_name == "Jack Bill"  # assert 为'断言'即是否满足特定条件
    # 运行方法,使用pytest 环境运行程序
