s1 = {1,2,3,4,5}
print(1 in s1)
print(6 in s1)
#not in
print("------------not in------------------")
print(1 not in s1)
print(6 not in s1)
#==
print("------------==--------------------")
print(s1)
s2 = {1,2,3,4,5}
print(s1==s2)
s2 = {2,3,4,5}
print(s1==s2)
print("---------is---------")
print(s1)
s2 = s1
print(s1 is s2)
s2 = {1,2,3}
print(s1 is s2)
print("------|-------")
s1 = {1,2,3,4}
s2 = {5,6,7,8}
print(s1 | s2)
print("--------&-------")
s1 = {1,2,3,4}
s2 = {2,4,6,8}
print(s1 & s2)
print("---------_--------")
print(s1)
print(s2)
print(s2-s1)
print("-------^------")
print(s1)
print(s2)
print(s1^s2)
print("-------->------")
print(s1)
print(s2)
print(s1>s2)