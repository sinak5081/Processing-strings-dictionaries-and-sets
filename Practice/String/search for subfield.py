#search for subfield
print("count:Returns the number of times a specified value occurs in a string")
s = "python programming"
print(s.count("python"))
s = "python python python"
print(s.count("python"))
print("__________________")
print("find:Searches the string for a specified value and returns the position of where it was found")
print(s)
print(s.find("python"))
s1 = "i love python so much"
print(s1.find("love"))
print(s1.find("python"))
print("______________________________")
print("index:Searches the string for a specified value and returns the position of where it was found")
print(s1)
print(s1.index("love"))
print("______________________________")
print("rfind:Searches the string for a specified value and returns the last position of where it was found")
s2 = "software engineer"
print(s2.rfind("engineer"))
print("__________________________")
print("rindex:Searches the string for a specified value and returns the last position of where it was found")
print(s2)
print(s2.rindex("software"))
print("__________________________")