# Sum of even numbers using while loop
def sum_of_even_numbers(n):
    total = 0
    i = 2
    print("Even numbers between 1 and", n, ":")
    while i <= n:
        print(i)
        total += i
        i += 2
    print("Sum of even numbers:", total)

# Sum of odd numbers using while loop
def sum_of_odd_numbers(n):
    total = 0
    i = 1
    print("Odd numbers between 1 and", n, ":")
    while i <= n:
        print(i)
        total += i
        i += 2
    print("Sum of odd numbers:", total)

def get_valid_input():
    while True:
        try:
            value = int(input("Enter a positive integer: "))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    try:
        n=get_valid_input()  # validation of positive integer input

        # Call functions to sum even and odd numbers
        sum_of_even_numbers(n) #call function to sum even numbers
        sum_of_odd_numbers(n) #call function to sum odd numbers
    except Exception as e:
        print("An unexpected error occurred:", e)