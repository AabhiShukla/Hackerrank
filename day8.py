n = int(input().strip())
phonebook = {}
for entry in range(n):
    line = input()
    name, number = line.split()
    phonebook[name] = number

for query in range(n):
    try:
        name = input()
    except EOFError:
        #EOF error is expected if no data is given when calling input
        break
    
    if name in phonebook:
        #print("{}={}".format(name, phonebook[name]))
        print(name+"="+phonebook[name])
    else:
        print("Not found")

