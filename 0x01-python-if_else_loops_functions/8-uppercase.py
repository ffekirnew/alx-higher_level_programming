def uppercase(str):
    for c in str:
        print(c if (ord(c) < 97) else chr(ord(c) - 32), end="")
    print()
