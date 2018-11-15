def ask_for_int():
    while True:
        try:
            res = int(input("Give me a number: "))
        except:
            print("WOW? Not a number")
            continue
        else:
            print("Thanks for the number")
            break
        finally:
            print("End of try/except/finally")

