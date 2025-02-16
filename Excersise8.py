# this is the practice of Chapter 8~~
# customize Pizza


def pizza_maker(inch, crust, *toppings):
    print(f"I want a {inch} inch {crust} Pizza\n")
    print("And I want these toppings:\n ")
    for topping in toppings:
        print(f"- {topping}")


crust_kind = ["thick", "crispy", "thin"]
for i in range(1, 3):
    pizza_maker(i, crust_kind[i], "Mushroom", "Pieapple")


def pizza_maker_dic(inch, crust, **pizza_info):
    pizza_info["inch"] = inch
    pizza_info["crust"] = crust
    return pizza_info


customize_pizza = pizza_maker_dic(15, "thick", toppings="Mushroom, Pieapple")
print(customize_pizza)


def pizza_maker_dic_list(**pizza_info):
    if "toppings" not in pizza_info:  # 空时先创建列表
        pizza_info["toppings"] = []
    needing = True
    while needing:
        topping = input("what : ")
        pizza_info["toppings"].append(topping)
        answer = input("Else?")
        if answer == "no":
            needing = False
    return pizza_info


pizza_file = pizza_maker_dic_list()
print(pizza_file)
