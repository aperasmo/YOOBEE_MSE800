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

if __name__ == "__main__":
    try:
        n = int(input("Enter a positive integer: "))
        if n < 1:
            raise ValueError("Number must be positive.") #validate input
        sum_of_even_numbers(n)
        sum_of_odd_numbers(n)
    except ValueError as e:
        print("Error:", e)