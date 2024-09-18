def implies(p,q):
    if p:
        return q
    else:
        return True
    
x = int(input("Input implication 1: "))
y = int(input("Input implication 2: "))
    
print(implies ( x >= 0 and y >= 0 , x * y >= 0 ))