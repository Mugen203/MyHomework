groceries = ""
def gro_list(groceries):
    # groceries = ""
    groceries = input("Please type in the groceries you need in your list or 'Exit' to leave: ")
    for word in groceries:
        if groceries != "Exit":
            print("This are the items you requested in your list: " + groceries)
        elif groceries == "Exit":
            break

gro_list(groceries)
