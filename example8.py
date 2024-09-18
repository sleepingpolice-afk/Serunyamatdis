def func():
    a = int(input("Input batas bawah: "))
    b = int(input("Input batas atas: ")) 
    for x in range(a, b):
        if (x-2 == 0):
            return True
    return False

result = func()
print(result)

#Ada beberapa input yang x-2 = 0 adalah benar, yaitu x = 2, makanya dinamakan existensial.