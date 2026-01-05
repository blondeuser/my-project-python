# # Day2: 30 Days of python programming
# first_name = "John"
# last_name = "Doe"
# full_name = f"{first_name} {last_name}"
# country = "Vietnam"
# city = "Saigon"
# age = 30
# year = 2026
# is_married = False
#
# first_name, last_name, full_name, country, city, age = (
#     "John",
#     "Doe",
#     "John Doe",
#     "Vietnam",
#     "Saigon",
#     30,
# )
#
#
# print(type(first_name), len(first_name))
# print(type(last_name), len(last_name))
# print(type(full_name), len(full_name))
# print(type(country), len(country))
# print(type(city), len(city))
# print(type(age))
#
# if len(first_name) > len(last_name):
#     print("The first name is longer than the last name.")
# else:
#     print("The last name is longer than the first name.")
#
#
def main():
    radius = 30
    result = area_of_circle(radius)
    print(f"Area of circle is: {result}")


def area_of_circle(r):
    return (r**2) * 3.14


main()
