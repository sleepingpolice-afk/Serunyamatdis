def func():
    a = int(input("Input batas bawah: "))
    b = int(input("Input batas atas: "))
    for x in range(a, b):
        for y in range(a, b):
            if x - y == 0:
                return True
    return False

result = func()
print(result)

# Untuk universal x dan existensial y, jika x-y = 0, maka akan return true. Dalam kondisi, ini a dan b harus sama untuk return false, kalau beda akan selalu return true, karena jika menggunakan for loop, akan ada minimal 1 kondisi yang akan memenuhi syarat.