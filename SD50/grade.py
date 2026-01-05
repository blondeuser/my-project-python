grade = int(input("Score: "))

if 90 <= grade <= 100:
    print("Grade A")
elif 80 <= grade < 90:
    print("Grade B")
elif 70 <= grade < 80:
    print("Grade C")
elif 60 <= grade < 70:
    print("Grade D")
else:
    print("Grade F")
