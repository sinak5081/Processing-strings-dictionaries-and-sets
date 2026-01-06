text = input("Enter a text:")
clean_text = text.strip()
lower_str = text.lower()
if text.startswith("hello") == True or text.startswith("HELLO"):
    print("Dont start with hello")
else:
    print(text)
    print(clean_text)
    print(lower_str)