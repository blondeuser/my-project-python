while True:
    try:
        x = int(input("what x? "))
        y = int(input("what y? "))
        break
    except ValueError:
        print("Please enter only interger.")
if x < y:
    print("x is less than y")
elif x == y:
    print(" x is equal y")
else:
    print(" x is greater than y")
