def greet_user():
    print("hello!")


greet_user()


# 传递列表test
def pass_users(users):
    for user in users:
        print("we have this user:", user)


users_list = ["john", "denis", "jackie", "bruto"]
pass_users(users_list)
# 函数修改列表
unprint_model = ["Y", "X", "Z"]
printed_model = []


def print_model_system(unprint_model, printed_model):
    while unprint_model:
        current_model = unprint_model.pop()
        print(f"{current_model} is complete")
        printed_model.append(current_model)


print_model_system(unprint_model, printed_model)
print(printed_model)
# 函数不修改列表,改用列表副本,不更改原始列表
unprint_model = ["Y", "X", "Z"]
printed_model = []


print_model_system(unprint_model[:], printed_model)
print(printed_model)
print("Original list:", unprint_model)


# 添加任意数量的实参
def tuple_add(*tuples):
    print(tuples)


tuple_add(233, 245, "hello")


# 任意数量形参,但是生成字典
def dic_add(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last name"] = last
    return user_info
    # 只知道传递的参数中,有姓名,但是其他信息不清楚,因此使用关键字实参


# 这个写法是错误的,因为应该采用的是关键字形参,而非具体键值名
# user_file = dic_add('Bill','D','Eat':'Meat','Age'=22)
user_file = dic_add("Bill", "D", eat="Meat", age="22")
print(user_file)
