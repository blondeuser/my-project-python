def main():
    names = ["Mario", "Luigi", "Yoshi", "Toad", "Bowser"]
    for name in names:
        if name == "Toad":
            print(write_letter(name, "Princess Peach"))


def write_letter(receiver, sender):
    return f"""
        Dear {receiver},
          it would be great if you could join us for a cozy dinner
          party at peach castle at tomorrow evening

          Best regards, 
          {sender}
          """


main()
