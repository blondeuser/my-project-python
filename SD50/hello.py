# add user their name
name = input("Enter username: ").strip().title()

# Remove white space from str
# name = name.strip().title()
# capitalize username
# name = name.capitalize()
# Split fistname and last name
first, middle, last = name.split()

# Say greeting to user
print(f"Greeting! {first}")
print(middle)
print(last)
