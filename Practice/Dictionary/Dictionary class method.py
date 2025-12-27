#method clear:	Removes all the elements from the dictionary
dic = {
    "Iran": "Tehran",
    "America":"Washington",
    "Germany":"Berlin",
    "France" : "Paris"
}
print(dic)
print(dic.clear())
print("_______________________________")
#method get:Returns the value of the specified key
dic = {
    "Iran": "Tehran",
    "America":"Washington",
    "Germany":"Berlin",
    "France" : "Paris"
}
val = dic.get("Germany")
print(val)
print("________________________________")
#method keys:Returns a list containing the dictionary's keys
for x in dic.keys():
    print(x)
#second method
val = dic.keys()
print(val)
print("________________________________")
#method values:Returns a list of all the values in the dictionary
for val in dic.values():
    print(val)
#second method
val = dic.values()
print(val)
print("________________________________")
#method item:Returns a list containing a tuple for each key value pair
val = dic.items()
print(val)
#second method
for x,y in val:
    print(x,y)
print("________________________________")
#method update:Updates the dictionary with the specified key-value pairs
print(dic)
a = {"England":"London"}
dic.update(a)
print(dic)
print("________________________________")
#method copy:Returns a copy of the dictionary
print(dic)
copy = dic.copy()
print("copy of dictionary")
print(copy)
print("________________________________")
#method pop:Removes the element with the specified key
print(dic)
print("After deleting:")
x = dic.pop("Iran")
print(x)
print(dic)
print("________________________________")
#method Setdefault:Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
print(dic)
d = dic.setdefault("Germany")
print(d)
d = dic.setdefault("Iran")
print(d)
print(dic)
print("________________________________")
#method Fromkeys:Returns a dictionary with the specified keys and value
state = ("America","Germany","Iran")
d = dic.fromkeys(state)
print(d)
d["Iran"] = "Tehran"
print(d)
d["America"] = "Washington"
d["Germany"] = "Berlin"
print(d)