import numpy as np

matrix1 = [[12.2, 11.8, 13.1, 11, 3.9, 4.1, 10.3, 8.4, 9.3],
           [10.9, 5.7, 13.5, 9.4, 11.4, 15.7, 10.8, 14],
           [12.7, 19.9, 13.6, 11.7, 18.3, 14.3, 22.8, 20.4]]

G, y, n, m, temp = 0, 0, 0, 0, []
for i in range(len(matrix1)):
    l = len(matrix1[i])
    temp.append((sum(matrix1[i]) ** 2)/l)
    n += l
    m += 1
    for j in range(l):
        G += matrix1[i][j]
        y += matrix1[i][j] ** 2

GSquareByN = G**2 / n
tr = sum(temp) - GSquareByN
tt = y - GSquareByN
te = tt - tr

print('matrix1', matrix1)
print('\nG: sumOf(matrix[i][j])', G)
print('GSquareByN:', GSquareByN)
print('sumOf(yij**2):', y)
print('tss:', tt)

print('\nt .i **2:', temp)
print('sst(sr**2):', tr)

print('\nsse(se**2): tss - sr**2:', te)
se = te/(m-1)
print('\nse**2: sse(se**2)/(n1+n2-1):', te, '/', m-1, ':', se)

print("\nANOVA Table")
print('Variation Source, SS, DF, MSS, VR')
print('Row, Error, total')
print(tr, ',', te, ',', tt)
print(m-1, ',', n-m, ',', n-1)
print(tr/(m-1), ',', te/(n-m))
print(tr/((m-1)*(te/(n-m))))