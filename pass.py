def do_nothing():
    pass


start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

if start > end:
    print("Invalid input, end number should be greater than starting number!")
else:
    # storing numbers
    numbers = []

    for i in range(start, end+1):
        if i % 2 == 0:
            # Add the number to the list
            numbers.append(i)
        else:
            # But if i is odd, do nothing
            pass

    # Print the even numbers
    print("Even are numbers:", *numbers)
