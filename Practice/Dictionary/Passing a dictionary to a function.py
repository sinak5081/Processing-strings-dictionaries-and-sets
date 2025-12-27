def DicInsert(dic):
    state, center = input("Enter a state,center: ").split()
    dic[state] = center
def dicSearch(dic):
    state = input("Enter state to search:")
    if state in dic:
        print("{0:10s} {1:10s}".format("state","center"))
        print("{0:10s} {1:10s}".format(state,dic[state]))
    else:
        print("state",state,"not found")
    input("Press key to continue:")
def dicDisplay(dic):
    print("{0:10s} {1:10s}".format("state","Center"))
    print("-" * 20)
    for state in dic:
        print("{0:10s} {1:10s}".format(state,dic[state]))
def dicUpdate(dic):
    state , center = input("Enter state,center: ").split()
    d = {state:center}
    dic.update(d)
def dicDelete(dic):
    state = input("Enter state to delete:")
    if state in dic:
        del dic[state]
        print("state",state,"Deleted")
    else:
        print("state",state,"Not found")
    input("press key to continue:")
def menu():
    print("1.Enter data to dictionary")
    print("2.search a state")
    print("3.Delete a state")
    print("4.Update the state center")
    print("5.Display the contents of dictionary")
    print("6.Exit")
    choice  = int(input("Enter your select (1-6):"))
    return choice
dic = dict()
while True:
    c = menu()
    if c ==1:
        DicInsert(dic)
    elif c ==2:
        dicSearch(dic)
    elif c ==3:
        dicDelete(dic)
    elif c ==4:
        dicUpdate(dic)
    elif c ==5:
        dicDisplay(dic)
    else:
        break