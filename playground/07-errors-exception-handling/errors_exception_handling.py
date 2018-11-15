"""
Nothing here, sorry!
"""


def ask_for_int():
    """
    @retrun: nothing
    """
    while True:
        try:
            res = int(input("Give me a number: "))
        except TypeError:
            print("WOW? Not a number")
            continue
        else:
            print(f"Thanks for the number {res}")
            break
        finally:
            print("End of try/except/finally")
