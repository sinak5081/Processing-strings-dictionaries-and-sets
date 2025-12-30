str = input("Enter a sentence: ")
print(str.title())
print("__________________")
#no method
result = ""
new_word = True
for ch in str:
    if new_word and 'e' <= ch <= 'z':
        result += chr(ord(ch) - 32)
        new_word = False
    else:
        result += ch
        if ch == ' ':
            new_word = True
        else:
            new_word = False
print(result)