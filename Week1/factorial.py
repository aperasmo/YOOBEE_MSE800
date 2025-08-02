def factorial(x):
    if x < 0: # Check if the input is negative
        raise ValueError("Negative numbers are not accepted.")
    elif x == 0:
        return 1
    else:
        result = 1
        for i in range(1, x + 1):
            print(i) # print the current number in the loop
            result *= i
        return result

if __name__ == "__main__":
    try:
        num = int(input("Enter a number to calculate its factorial: ")) #input any postive number 
        print(f"Factorial of {num} is {factorial(num)}")
    except ValueError as e:
        print(f"Error: {e}")    # raise an error if input is not a valid integer	