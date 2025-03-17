# Calculate the factorial
# Using while loop

number = int(input("Enter a positive number: "))

fac = 1
i = 1

if number >= 0:
	while i <= number:
		fac *= i
		i += 1
else:
	print("Factorial is no defined for negative numbers.")
print("Factorial of the number is", fac)
