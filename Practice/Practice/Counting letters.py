str = input("Enter a string:")
print("Number of letters:",len(str))
count_a =str.count("a") + str.count("A")
print("Number of letters a:",count_a)
#without method
print("______________________")
print("without method:")
count = 0
countt = 0
for latter in str:
    count += 1
    if latter == "a" or latter == "A":
        countt += 1
print(countt)
print(count)