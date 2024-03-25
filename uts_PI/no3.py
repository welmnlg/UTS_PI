"""
                UTS
Nama    : Imanuel M.T. Manullang
NIM     : 221402036
Matkul  : Pemrograman Integrative

Soal 3:
Write a Python program that reads in a number and prints the date that number of days from now in this format: Monday on 25 March 2024.

"""
from datetime import datetime, timedelta

days = int(input("Masukkan tanggal hari ini: "))

result_date = (datetime.now() + timedelta(days=days)).strftime("%A on %d %B %Y")

print(f"Tanggal yang sejumlah tanggal hari ini: {result_date}")

