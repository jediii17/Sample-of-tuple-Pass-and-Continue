
n = int(input("Enter the range of numbers: "))
numbers = input("Enter a list of numbers separated by commas: ")

number_list = numbers.split(',')

# convert the strings in the list to integers
for i in range(len(number_list)):
    number_list[i] = int(number_list[i])

# check number is equal to the range
if len(number_list) != n:
    print("Invalid input, too many input numbers")
else:
    # initialize variables to store the largest and lowest numbers
    largest = -1
    lowest = n+1

    # find the largest and lowest numbers in the list
    for num in number_list:
        if num > largest:
            largest = num
        if num < lowest:
            lowest = num
        if num < 0 or num > n:
            continue

    print("Largest number:", largest)
    print("Lowest number:", lowest)
