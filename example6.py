def implies(p,q):
    if p:
        return q
    else:
        return True
    
x = 0
y = 0
    
print(implies ( x >= 0 and y >= 0 , x * y >= 0 ))

# fix later