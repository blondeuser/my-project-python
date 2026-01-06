# def main():
#     print_column(23)
#
#
# def print_column(height):
#     for _ in range(height):
#         print("#")
#
#
# main()


# def main():
#     print_row(4)
#
#
# def print_row(width):
#     print("?" * width)
#
#
# main()
#
# def main():
#     brick(3)
#
#
# def brick(size):
#     for _ in range(size):
#         print("***")
#
#
# main()


def main():
    print_brick(10)


# define brick printer
def print_brick(size):
    # print 3 time down the line
    for i in range(size):
        # print 3 time on the line
        for j in range(size):
            # print # without down a line
            print("#", end="")
        # print the line
        print()


main()
