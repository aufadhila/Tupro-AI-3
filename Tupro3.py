from xlrd import open_workbook
import numpy as np
import math

workbook = open_workbook('D:\Kuliah\Matkul\Semester 5\AI\TUPRO 3\DatasetTugas3AI1718.xlsx')
datatrain = workbook.sheet_by_index(0)
datatest = workbook.sheet_by_index(1)

A1 = []
A2 = []
B1 = []
B2 = []
C1 = []
C2 = []
D1 = []
D2 = []
n1 = []
n2 = []
hasil = []
hasil1 = []
data = []

def carijarak (A1, A2, B1, B2, C1, C2, D1, D2) :
    hasil = (A1 - A2) ** 2 + (B1 - B2) ** 2 + (C1 - C2) ** 2 + (D1 - D2) ** 2
    Akar = math.sqrt(hasil)
    return Akar

for i in range(1, datatrain.nrows):
    A1.append(datatrain.cell_value(i, 1))
    B1.append(datatrain.cell_value(i, 2))
    C1.append(datatrain.cell_value(i, 3))
    D1.append(datatrain.cell_value(i, 4))
    n1.append(datatrain.cell_value(i, 5))

for i in range(1, datatest.nrows):
    A2.append(datatest.cell_value(i, 1))
    B2.append(datatest.cell_value(i, 2))
    C2.append(datatest.cell_value(i, 3))
    D2.append(datatest.cell_value(i, 4))
    n2.append(datatest.cell_value(i, 5))

for i in range(1000) :
    tes = 0
    tes1 = 0
    hasil = []
    hasil3 = 0
    y = []
    z = []
    hoax = 0
    tidak_hoax = 0

    for j in range(1000,len(A1)) :
        hasil3 = carijarak(A1[j] , A1[i] , B1[j] , B1[i] , C1[j] , C1[i] , D1[j] , D1[i])
        hasil.append(hasil3)
    for i in range(25) :
        if n1[hasil.index(min(hasil))] == 1 :
            tes += 1
        else:
            tes1 += 1
        hasil.remove(min(hasil))
    nilai = 0
    if tes > tes1 :
        nilai = 1
    data.append(nilai)
for i in range(1000) :
    if data[i] == n1[i] :
        hoax += 1
print hoax/10

del data[:]
del hasil[:]

for i in range(1000) :
    tes = 0
    tes1 = 0
    hasil = []
    hasil3 = 0
    y = []
    z = []
    hoax = 0
    tidak_hoax = 0

    for j in range(len(A1)) :
        hasil3 = carijarak(A1[j] , A2[i] , B1[j] , B2[i] , C1[j] , C2[i] , D1[j] , D2[i])
        hasil.append(hasil3)
    for i in range(25) :
        if n1[hasil.index(min(hasil))] == 1 :
            tes += 1
        else:
            tes1 += 1
        hasil.remove(min(hasil))
    nilai = 0
    if tes > tes1 :
        nilai = 1
    data.append(nilai)
print data