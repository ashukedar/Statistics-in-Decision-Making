import numpy as np

matrix1 = [[3.0, 2.4, 1.9, 2.2, 1.7],
           [2.1, 2.7, 2.3, 2.5, 3.1],
           [2.1, 2.6, 2.5, 2.9, 2.1],
           [2.0, 2.5, 3.2, 2.5, 2.2],
           [2.1, 3.6, 2.4, 2.4, 2.1]]

G, y, n, temp = 0, 0, len(matrix1), []
for i in range(len(matrix1)):
    temp.append((sum(matrix1[i]) ** 2)/n)
    for j in range(n):
        G += matrix1[i][j]
        y += matrix1[i][j] ** 2

temp2 = []
matrix2 = [[matrix1[j][i] for j in range(len(matrix1))] for i in range(len(matrix1[0]))]
for i in range(len(matrix2)):
    temp2.append((sum(matrix2[i]) ** 2)/n)

k = 0
temp3 = [0] * n
for i in range(n):
    for j in range(n):
        temp3[k%n] += matrix1[i][j]
        k += 1
    k += 1
for i in range(n):
    temp3[i] = temp3[i] ** 2 / n

GSquareByN = G**2 / (n**2)
tc = sum(temp2) - GSquareByN
tr = sum(temp) - GSquareByN
td = sum(temp3) - GSquareByN
tt = y - GSquareByN
te = tt - tc - tr - td

print('matrix1', matrix1)
print('matrix2', matrix2)
print('n1:', n)
print('n2:', n)
print('\nG: sumOf(matrix[i][j])', G)
print('GSquareByN:', GSquareByN)
print('sumOf(yij**2):', y)
print('tss:', tt)

print('\nt .i. **2:', temp)
print('sst(sr**2):', tr)

print('\nt i.. **2:', temp2)
print('sst(sc**2):', tc)

print('\nt ..i **2:', temp3)
print('sst(sd**2):', td)

print('\nsse(se**2): tss - sr**2 - sc**2 - sd**2:', te)
se = te/((n-1)*(n-2))
print('\nse**2: sse(se**2)/((n1-1)*(n2-1)):', te, '/', ((n-1)*(n-1)), ':', se)

fr = tr/(se*(n-1))
fc = tc/(se*(n-1))
fd = td/(se*(n-1))
print('\nfr: sst(sr**2)/(se**2*(n2-1)):', tr, '/', se*(n-1), ':', fr)
print('\nfc: sst(sc**2)/(se**2*(n1-1)):', tc, '/', se*(n-1), ':', fc)
print('\nfd: sst(sd**2)/(se**2*(n1-1)):', td, '/', se*(n-1), ':', fd)

print("\nANOVA Table")
print('Variation Source, SS, DF, MSS, VR')
print('Row, Col, Diagonal, Error, total')
print(tr, ',', tc, ',', td, ',', te, ',', tt)
print(n-1, ',', n-1, ',', n-1, ',', (n-1)*(n-2), ',', n**2-1)
print(tr/(n-1), ',', tc/(n-1), ',', td/(n-1), ',', te/((n-1)*(n-2)))
print(tr/((n-1)*(te/((n-1)*(n-2)))), ',', tc/((n-1)*(te/((n-1)*(n-2)))), ',', td/((n-1)*(te/((n-1)*(n-2)))))