#with method
#__________________
def repetition(str,str1):
    print(str1.count(str))
s = input("Enter a Word:")
s1 = input("Enter a sentence:")
repetition(s,s1)
print("______________________________")
#no method
count = 0
for i in range(len(s1) - len(s)+1):
    if s1[i:i+len(s)] == s:
        count += 1
print(count)