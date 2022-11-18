import math
panjangDinding = int (input("Masukan Panjang :"))
lebarDinding = int (input("Masukan Lebar :"))
jariDinding = int (input("Masukan Jari-jari :"))
luasling = float((3.14*(jariDinding**2)/2))
luasPersegi = float(panjangDinding*lebarDinding)
jumlahCat = float(((luasling+luasPersegi)/15))
print ("Area tersebut mebutuhkan",math.ceil(jumlahCat),"Kaleng cat ")
