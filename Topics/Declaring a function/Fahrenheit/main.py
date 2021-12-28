# def fahrenheit_to_celsius(x):
#     return round((x - 32) * 5 / 9, 3)

name = "John"

def change_name(new_name):
    global name
    name = new_name

change_name("Mary")
print(name)
