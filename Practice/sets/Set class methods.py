#method add:Adds an element to the set
fruits = {"apple","banana","cherry"}
print(fruits)
fruits.add("orange")
print(fruits)
print("____________________________________")
#method clear:Removes all the elements from the set
#method copy:Returns a copy of the set
a = fruits.copy()
print(a)
print(a.clear())
print("____________________________________")
#method difference:Returns a set containing the difference between two or more sets
a = {"apple","cherry","banana"}
b = {"Google","Microsoft","apple"}
print(set.difference(a,b))
print("____________________________________")
#method symmetric_difference:Returns a set with the symmetric differences of two sets
print((a-b)|(b-a))
print("____________________________________")
#method issubset:Returns True if all items of this set is present in another set
print(a)
print(b)
print(a.issubset(b))
print("____________________________________")
#method discard:Remove the specified item
print(a)
a.discard("apple")
print(a)
print("____________________________________")
#method issuperset:	Returns True if all items of another set is present in this set
x = {1,2,3,4}
y = {2,4,6}
print(x.issuperset(y))
y = {2,4}
print(x.issuperset(y))
print("____________________________________")
#method union:Return a set containing the union of sets
print(a)
print(b)
print(a.union(b))
print("____________________________________")
#method intersection:Returns a set, that is the intersection of two other sets
print(a)
a.add("apple")
print(a)
print(b)
print(a.intersection(b))
print("____________________________________")
#method isdisjoint:	Returns whether two sets have a intersection or not
print(a)
print(b)
print(a.isdisjoint(b))
print(x)
print(a)
print(x.isdisjoint(a))
print("____________________________________")
#method pop:Removes an element from the set
print(a)
print(a.pop())
print(a)
print("____________________________________")
#method update:Update the set with the union of this set and others
print(x)
print(a)
set.update(x,a)
print(x)
print("____________________________________")
#method remove:	Removes the specified element
print(x)
x.remove(1)
print(x)
print("____________________________________")
#method intersection_update():Removes the items in this set that are not present in other, specified set(s)
print(a)
print(x)
x.intersection_update(a)
print(x)
print("____________________________________")
#method Inserts the symmetric differences from this set and another
a.add("apple")
print(a)
print(b)
a.symmetric_difference_update(b)
print(a)