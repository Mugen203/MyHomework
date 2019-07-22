groceries = []
def gro_list(groceries):
    input = ""
    while input != "Exit":
        break
        groceries = input("Please type in the groceries you need in your list or 'Exit' to leave: ")
        for word in groceries:

            print("This is the number of items going to be in your list = ", len(groceries))
            print("This are the items you requested in your list: " + groceries)
gro_list(groceries)
