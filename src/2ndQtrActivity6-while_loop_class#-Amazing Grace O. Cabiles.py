# this variable will be used later for the max()
largest_num = 0

# prompts the user
num = int(input("Enter a number or type -1 to end the program: "))

# infinite loop
while True:
    # if num != -1 its going to keep promping the user for a number
    if num != -1:
        num = int(input("Enter a number or type -1 to end the program: "))
        # any number inputted above gets stored in the largest_num
        # max() will check which one is the largest number in all of the inputted numbers
        largest_num = max(largest_num, num)
    elif num == -1:
        largest_num = max(largest_num, num)
        # after the maximum or largest number number is found we turn it into a string
        # so we can print the largest number out on the screen then the program stops
        largest_num = str(largest_num)
        print("The largest number is", largest_num)
        break
    else:
        num = int(input("Enter a number or type -1 to end the program: "))
        largest_num = max(largest_num, num)
        continue
