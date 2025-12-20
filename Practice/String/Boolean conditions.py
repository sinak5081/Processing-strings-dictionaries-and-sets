#Testing Boolean conditions
print("startWith:Returns true if the string starts with the specified value")
s = "hello world"
print(s)
print(s.startswith("h"))
print(s.startswith("t"))
print("_____________________________________________")
print("endwith:Returns true if the string ends with the specified value")
print(s)
print(s.endswith("t"))
print(s.endswith("d"))
print("_____________________________________________")
print("isspace:Returns True if all characters in the string are whitespaces")
print(s)
s1 = "  "
print(s.isspace())
print(s1)
print(s1.isspace())
print("_____________________________________________")
print("isalpha:Returns True if all characters in the string are in the alphabet")
s = "helloworld"
print(s)
print(s.isalpha())
s1 = "sina123"
print(s1)
print(s1.isalpha())
s1 = "sina karimi"
print(s1)
print(s1.isalpha())
print("_____________________________________________")
print("islower:Returns True if all characters in the string are lower case")
s1 = "Hello World"
print(s1)
print(s1.islower())
s1 = "hello world"
print(s1)
print(s1.islower())
print("_____________________________________________")
print("isupper:Returns True if all characters in the string are upper case")
print(s1)
print(s1.isupper())
s1 = "HELLO WORLD"
print(s1)
print(s1.isupper())
print("_____________________________________________")
print("isdigit:Returns True if all characters in the string are digits")
print(s1,s1.isdigit())
s1 = "12345"
print(s1,s1.isdigit())
print("_____________________________________________")
print("isdecimal:Returns True if all characters in the string are decimals")
print(s1)
print(s1.isdecimal())
s1 = "hello world12"
print(s1)
print(s1.isdecimal())
print("_____________________________________________")
print("isnumeric:Returns True if all characters in the string are numeric")
s1 = "15"
print(s1)
print(s1.isnumeric())
print("_____________________________________________")
print("isalnum:Returns True if all characters in the string are alphanumeric")
s1 = "sina17"
print(s1)
print(s1.isalnum())