# Chapter 9 class
# Skip module part,类中函数即方法
# __init__()方法: 创建类时自动执行,初始化对象属性,只执行一次,本类均调用
# 其余函数需传入self参数
class Restaurant:
    def __init__(self, name, cuisine):
        self.restaurant_Name = name
        self.cuisine_Type = cuisine
        self.customer_num = 0  # default number of customer

    def describe_restaurant(self):
        print(
            f"Our restaurant name is {self.restaurant_Name},and we provide {self.cuisine_Type}"
        )

    def customer_update(self, number):
        if number >= self.customer_num:
            self.customer_num = number
            print(f"The most number of customer is {self.customer_num}")

        else:
            print(f"The most number of customer is {self.customer_num}")

    def open_restaurant(self):
        print("We are opening!")


first_Restaurant = Restaurant("Liaoning Cafe", "Meat and Vegetable")
first_Restaurant.describe_restaurant()
first_Restaurant.open_restaurant()
first_Restaurant.customer_update(0)
first_Restaurant.customer_update(5)


class SmallRestaurant(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)

    def open_restaurant(self):  # 重写方法
        print("Small restaurant is closed.")


second_restaurant = SmallRestaurant("Tieling", "Only meat")
second_restaurant.open_restaurant()
