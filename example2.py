def is_prime():
    N = int(input("Input sebuah angka: "))
    
    if N <= 1:
        return False 

    for i in range(2, int(N**0.5) + 1): 
        if N % i == 0 and (i != 1 and i != N):
            return False 
    
    return True 

result = is_prime()
print("Is prime:", result)
# Cek angka apakah bilangan prima atau bukan. Jika bilangan adalah prima, maka program akan menghasilkan output True, dan jika bilangan bukan
# prima, maka program akan menghasilkan output False.