"""
                UTS
Nama    : Imanuel M.T. Manullang
NIM     : 221402036
Matkul  : Pemrograman Integrative
Soal 3:
Write a program that reads in integer numbers from a text file named input.txt in the same directory as the executing program.
Print the sum of the numbers with comma separators and three digits.
"""
with open('input.txt', 'r') as file:
    numbers = map(int, file.read().split())

total_sum = sum(numbers)
final_sum = '{:,.3f}'.format(total_sum)
print(f"Jumlah angka (3 digit di belakang koma):{final_sum}")
