str = input("Enter a string:(Number and sentence):")
if str.isalpha() == True:
    print("It's just letters.")
elif str.isdigit() == True:
    print("Only numbers between 0 and 9")
elif str.isalnum() == True:
    print("The sentence and the letters are together.")
else:
    print("String Error")