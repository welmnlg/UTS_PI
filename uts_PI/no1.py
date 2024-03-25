"""
                UTS
Nama    : Imanuel M.T. Manullang
NIM     : 221402036
Matkul  : Pemrograman Integrative

Soal 1:
Write a Python program that reads in a whole number and divides it by number of days this year and displays the result with eleven decimal places if they exist (rounded up).

"""

import datetime

this_year = datetime.datetime.now().year

number_of_days = (datetime.date(this_year + 1, 1, 1) - datetime.date(this_year,1,1)).days

whole_number = int(input("Masukkan bilangan bulat: "))

result = whole_number/number_of_days

final_result = "{:.11f}".format(result)

print("Hasil: ", final_result)