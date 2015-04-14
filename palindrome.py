import sys

text = sys.argv[1]

def palindrome(text):
    x = ''
    for t in text:
        if t.isalnum():
            x += t
            
    return x == x[::-1]

print(palindrome(text))
