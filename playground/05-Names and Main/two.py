import one

print("TOP LEVEL in two.py")

one.func()

if __name__ == "__main__":
    print("two.py is been run directly")
else:
    print("two.py has been imported!")

