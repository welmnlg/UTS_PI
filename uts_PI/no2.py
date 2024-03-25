"""
                UTS
Nama    : Imanuel M.T. Manullang
NIM     : 221402036
Matkul  : Pemrograman Integrative

Soal 2:
Write a Python program that reads a number (today's test date) and prints the product of all the values from 1 to that number.

"""
test_date = int(input("Tanggal tes hari ini: "))
sum = 1

for i in range(1, test_date + 1):
    print(i, end=" ")
for i in range(1, test_date + 1):
    sum *= i

print(f"\n\nProduct of all the values from 1 to {test_date} is: {sum}")

