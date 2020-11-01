print("pilih opsi yang ada inginkan")
print("1. Penjumlahan")
print("2. Pembagian")

p = int(input("masukkan pilihan (1/2) :"))
a = int(input("masukkan bilangan pertama :"))
b = int(input("masukkan bilangan kedua :"))

if p == 1 :
    jlh = a+b
    print(a,"+",b,"=",jlh)

elif p == 2 :
    bagi = a/b
    print(a,"/",b,"=",bagi)