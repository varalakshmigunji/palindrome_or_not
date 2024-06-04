def is_palindrome(input_string):
    # Convert input string to lowercase to ignore case
    input_string = input_string.lower()
    
    # Remove non-alphanumeric characters
    input_string = ''.join(char for char in input_string if char.isalnum())
    
    return input_string == input_string[::-1]
print(is_palindrome("racecar"))
print(is_palindrome("madam"))  
print(is_palindrome("intern"))  
print(is_palindrome("malayalam"))  