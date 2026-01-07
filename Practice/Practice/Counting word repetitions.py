str = input("Enter a sentence:")
word = str.split()
count = {}
for word in word:
    count[word] = count.get(word,0) + 1
print(count)