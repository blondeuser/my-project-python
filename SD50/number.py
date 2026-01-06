def main():
    result = get_int()
    print(f"x is {result}")

def get_int():
    while True:
        try:
            x = int(input("what x? "))
        except ValueError:
            print("x is not an int! ")
        else:
            break
    return x

main()
