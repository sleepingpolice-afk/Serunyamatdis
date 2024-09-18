def is_prime():
    N = int(input("Input sebuah angka: "))
    
    if N <= 1:
        return False 

    for i in range(2, int(N**0.5) + 1): 
        if N % i == 0:
            return False 
    
    return True 

result = is_prime()
print("Is prime:", result)
# Return Boolean True atau False