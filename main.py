
def getInput():
    my_string = input("Enter multiple values") # Prompt user
    my_string_values = my_string.split() # Split input into list of strings
    my_string_ints = [int(n) for n in my_string_values] # Convert to integers
    return my_string_ints


def listSum(list1, list2):


def main():
    list1 = getInput()
    list2 = getInput()
    ret = listSum(list1, list2)
    print(f'The result values are: {ret}')


if __name__ == '__main__':
    main()
