i = int(input("Masukkan batas bawah: "))
k = int(input("Masukkan batas atas: "))

A= set([x for x in range (i, k) if x**2+x-6==0])
B = set([2, -3])

print(A==B)
