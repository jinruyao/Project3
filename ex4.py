# Prompt the user for their age
# Using if & elif & else

a = input("Enter your age: ")
age = int(a)

if age <= 19:
	print("You can qulify for student discounts.")
elif age > 19 & age <=54:
	print("You qulify for no age discounts.")
else:
	print("You can receive senior discounts.")

