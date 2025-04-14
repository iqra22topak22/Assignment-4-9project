
def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """

    print(lst[0])

# There is no need to edit code beyond this point

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)


if __name__ == '__main__':
    main()


# --------------------------------------------------------------------

def get_first_ele(lst):
    print(lst[0])

def get_ele():
    lst = []
    ele :str = input("plese enter first element")

    while ele !="":
        lst.append(ele)
        ele = input("please enter element")

        return lst
    
def main():
    lst =get_ele()
    get_first_ele(lst)

if __name__ == '__main__':
    main()


