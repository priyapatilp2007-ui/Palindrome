string = input("Enter a string: ")

reverse_string = string[::-1]

if string.lower() == reverse_string.lower():
    print("The given string is a Palindrome")
else:
    print("The given string is not a Palindrome")