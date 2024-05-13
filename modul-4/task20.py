'''Write python program that user to enter only odd numbers, else will
raise an exception.'''
while True:
    try:
        num = int(input("Please enter an odd number: "))
        if num % 2 != 0:
            print("You entered:", num)
            break
        else:
            raise ValueError("You entered an even number. Please enter an odd number.")
    except ValueError as ve:
        print(ve)

