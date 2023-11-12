def is_palindrome(word):
    reversed_word = ''
    for char in word:
        reversed_word = char + reversed_word
    return word == reversed_word

# Example usage:
result = is_palindrome("abba")
print(result)  # Output: True
