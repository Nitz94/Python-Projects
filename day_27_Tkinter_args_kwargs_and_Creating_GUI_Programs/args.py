# setting unlimited arguments for a function using * operator. the arguments are denoted by args notation by default
# these are positional arguments. * operator collects the arguments as a tuple and take any number of arguments

def add(*args):
    answer = 0
    for number in args:
        answer += number

    return answer


# print(add(10, 20, 30, 40, 50))


# unlimited key word arguments using ** operator. the arguments are packed inside kwargs or keyword arg as a dictionary

def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():  # we can loop through kwargs like a dictionary
    #     print(key)
    #     print(value)
    n += kwargs["multiply"]  # takes the value under multiply and adds it with n then
    n *= kwargs["add"]       # takes the value under add and multiplies with n
    n += kwargs["test"]
    # print(n)


# calculate(2, add=3, multiply=5, test=25)  # kwargs can take any number of keyword arguments.
# it gives a way to name the values which are passing into the function

# creating a class with many keyword arguments

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")    # instead of kwargs["make"]
        self.model = kwargs.get("model")
        self.year = kwargs.get("year")
        self.color = kwargs.get("color")
        # when calling items in kwargs get method is preferred. when kwargs["key"] method is used and there is no such
        # key it will return error. but when get method is used if there is no such key none is returned and the rest
        # of the code is executed.


my_car = Car(make="Toyota", model="GR-Corolla", year="2022")
print(my_car.model)
print(my_car.make)
print(my_car.color)
print(my_car.year)
