def main():
    lst = []  

    val = input("Enter a value: ") 
    while val: 
        lst.append(val) # Add val to list
        val = input("Enter a value: ")  # Get the next value to add

    print("Here's the list:", lst)


if __name__ == '__main__':
    main() 



