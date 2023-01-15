# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

# Check the data type of two_digit_number.
print(type(two_digit_number))

# Get the first and second digit using subscripting, then convert string to integer.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# Add the two digits together.
total = first_digit + second_digit

print(total)
