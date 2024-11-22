def is_palindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]

