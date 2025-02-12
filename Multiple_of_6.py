def get_multiple_6():
    """
    Returns a multiple of 6 that was entered by the user
    :return: int a number
    """
    try:
        n = input("Please give me a multiple of 6: ")
        n = int(n)
        #How do we check if something is a multiple of 6?
        if n % 6 == 0:
            return n
        else:
            print("that's not a multiple of 6")
    except ValueError:
        print("you have not entered a number")

get_multiple_6()