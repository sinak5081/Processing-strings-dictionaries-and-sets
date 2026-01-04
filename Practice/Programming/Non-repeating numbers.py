num = []
while len(num) < 20:
    x = int(input("Enter a number between(1-100): "))
    if x < 1 or x > 100:
        print("not between(1-100)")
    elif x in num:
        print("The number is repeated.")
    else:
        num.append(x)
print("list of number")
print(num)