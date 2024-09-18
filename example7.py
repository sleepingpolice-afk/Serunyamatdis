def func():
    x = int(input("Input batas bawah: "))
    y = int(input("Input batas atas: ")) 
    for x in range(x, y):
        if not (x**2 >= 0):
            return False
        return True

result = func()
print(result)
