# looping dai list

# for loop
print("For Loop")
kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["kelana","angan","raka","dira"]

for nama in peserta:
    print(f"nama = {nama}")

# for loop and range
print("\nLoop and Range")
kumpulan_angka = [10,5,4,2,5,6]

panjang = len (kumpulan_angka)


for i in range (panjang):
    print(f"angka = {kumpulan_angka[i]}")

# while
print("\nWhile Loop")
kumpulan_angka = [10,5,4,2,5,6]

panjang = len (kumpulan_angka)
i = 0
while i < panjang:
    print(f"angka ={kumpulan_angka[i]}")
    i += 1

# list comprehension

print("\nList Comprehension")
data = ["ucup",1,2,3,"otong"]

[print(f"data={i}") for i in data]

angka = [10,5,4,2,6,5]

angka = [10,5,4,2,6,5]

angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# Enumerate

print("\n Eumerate")
data_list = ["ucup",1,2,3,]

for index,data in enumerate(data_list):
    print(f"index = {index}, data = {data}")