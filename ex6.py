# Calculate the factorial
# Using for loop

number = int(input("Enter a positive number: "))

fac = 1

if number >= 0:
        for i in range(1, number + 1):
                fac *= i
else:
        print("Factorial is no defined for negative numbers.")
print("Factorial of the number is", fac)
