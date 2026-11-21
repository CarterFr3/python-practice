# CREATE self adding and removing list
# Needs to have user input
# Needs to have options e.g - choices 1, 2, or 3
# Needs to be appended to the list
# Needs to display what was added
# Need to add a break to end the list

list = []

while True:
    print("Options: \n1) Add to List \n2) Remove from list \n3) Quit")
    choices = input("Choose 1, 2, or 3: ")
    if choices == "1":
        add = input("What do you want to add? ")
        list.append(add)
        print(list)
    elif choices == "2":
        list_count = len(list)
        if list_count == 0:
            print("You need to add something to remove something")
        else:
            removing_task = input(f"What would like to remove? {list}")
            if removing_task in list:
                list.remove(removing_task)
                print(list)
    else: 
        print("Quitting")
        break
            




    