
table = ["none"]*8
def hashf(s):
    b = s.encode()
    
    total =  0

    for i in b: 
        total += 1
    return total


print(hashf("Beej"))
print(hashf("Goats"))
print(table)


def put(key, value):
    #which slot in the table is the value going and 
    #store value at that slot
    
    pass

def get(key):
    pass

def delete(key):
    pass


