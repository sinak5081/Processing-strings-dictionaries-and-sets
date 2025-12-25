#Accessing dictionary elements
dec = {
    "Iran" : "Tehran",
    "America" : "Washington",
    "Germany" : "Berlin",
    "France" : "Paris"
}
print(dec["Iran"])
print("_______________________")
#Operator in:
print("Germany" in dec)
print("________________________")
#Determining the length of the dictionary
print(len(dec))
print("________________________")
#Accessing dictionary elements with a for loop
print(dec)
for country in dec:
    print("{0:10s} {1:10s}".format(country,dec[country]))
print("_____________________________")
#Remove element from dictionary
print(dec)
del dec["Iran"]
print(dec)
print("______________________________")
#Add element to dictionary
print(dec)
dec["Iran"] = "Tehran"
print(dec)