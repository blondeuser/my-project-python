# age = int(input("Enter your age: "))
# height = int(input("Enter your height: "))
# # Enter base and height of the triangle
# print("Welcome, now enter following: ")
# base = float(input("Enter base of the triangle "))
# height_triangle = float(input("Enter height of the triangle "))
# area = 0.5 * base * height_triangle
# print(f"Area of the triangle is: {area}")
# print("Thanks, now enter following: ")
# side_a = float(input("Enter side a "))
# side_b = float(input("Enter side b "))
# side_c = float(input("Enter side c "))
# perimeter = side_a + side_b + side_c
# print(f"perimeter of the triangle is: {perimeter}")
##
# print(len("dragon") < len("python"))
# print("jargon" in "I hope this course is not full of jargon")

# hours = float(input("Enter hours: "))
# rate = float(input("Enter rate per hour"))
#
# weekly = hours * rate
# monthly = weekly * 4
# print(f"Your weekly earning is: {weekly}")
# print(f"Your monthly earning is: {monthly}")


# def main():
#     age = int(input("Enter the your age: "))
#     total_sec = second_elapse(age)
#     print(f"You have lived {total_sec} seconds!")
#
#
# def second_elapse(age):
#     second_in_year = 3153600
#     return age * second_in_year
#
#
# main()
import random


def main():
    user_age = int(input("Enter your age: "))
    death_age = death(user_age)
    year_left = time(death_age, user_age)
    print(f"You got: {year_left} year left!, Please enjoy your life responsibly")


def death(user_age):
    return random.randint(user_age + 1, 100)


def time(death_age, user_age):
    return death_age - user_age


main()
