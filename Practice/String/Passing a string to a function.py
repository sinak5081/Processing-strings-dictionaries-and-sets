#Cutting a string into substrings
#Sub-thread link
#Replacing characters in a string
#Doubt search under the thread
def change(string):
    print("split the string:")
    sp = string.split()
    print(sp)
    composite = ",".join(sp)
    print("composite:")
    print(composite)
    rep = composite.replace(",",":")
    print("Replace")
    print(rep)
    subStr = "Science"
    index = string.find(subStr)
    if index == -1:
        print(subStr,"not found")
    else:
        print(subStr,"found at index",index)
st = input("Enter a string:")
change(st)