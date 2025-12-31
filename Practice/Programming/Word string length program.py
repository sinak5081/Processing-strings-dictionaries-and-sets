def counting(str,m):
    words = str.split(" ")
    for word in words:
        if len(word)==m:
            print(word,"=>match successfully")
        else:
            print(word,"=>match Error")
s1 = input("Enter a string of word:")
num = int(input("Enter a num:"))
counting(s1,num)