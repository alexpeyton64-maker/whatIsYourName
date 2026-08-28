name = input("What is your name? ")
if name.endswith("Gumby"):
    print("Hello, Mr.Gumby")
if name.startswith("Mr."):
    print("Hello, " + name)
elif name.startswith("Mrs."):
    print("Hello, " + name)
else:
    print("Hello, " + name)
