def Display(dic):
    print(dic)
def DicInsert(dic):
    word = input("Enter word:")
    info = input("information for word:")
    dic[word] = info
def DicSearch(dic):
    word = input("Enter a word for search:")
    if word in dic:
        print(dic[word])
        print(word,"found")
    else:
        print(word,"is not found")
def dicDelete(dic):
    word = input("Enter a word for delete:")
    if word in dic:
        del dic[word]
        print("word",word,"deleted")
    else:
        print("word",word,"not found")
def menu():
    print("1.Enter data to dictionary:")
    print("2.search a word")
    print("3.delete a word")
    print("4.display the content")
    print("5.Exit")
    choice = int(input("Enter your select(1-5):"))
    return choice
dics = {"hello":"hi","how are you":"im fine","how old are you":17,"what is your name":"Sina"}
while True:
    c = menu()
    if c == 1:
        DicInsert(dics)
    elif c == 2:
        DicSearch(dics)
    elif c == 3:
        dicDelete(dics)
    elif c == 4:
        Display(dics)
    else:
        break