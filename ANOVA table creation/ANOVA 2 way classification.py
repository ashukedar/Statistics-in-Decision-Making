import numpy as np

matrix1 = [[20.6, 20.7, 20],
           [24.7, 26.5, 27.1],
           [25.2, 23.4, 21.6],
           [24.5, 21.5, 23.6]]

G, y, n, m, temp = 0, 0, 0, 0, []
for i in range(len(matrix1)):
    l = len(matrix1[i])
    temp.append((sum(matrix1[i]) ** 2)/l)
    n = max(n, l)
    for j in range(l):
        G += matrix1[i][j]
        y += matrix1[i][j] ** 2

temp2 = []
matrix2 = [[matrix1[j][i] for j in range(len(matrix1))] for i in range(len(matrix1[0]))]
for i in range(len(matrix2)):
    l = len(matrix2[i])
    temp2.append((sum(matrix2[i]) ** 2)/l)
    m = max(m, l)

GSquareByN = G**2 / (m*n)
tc = sum(temp2) - GSquareByN
tr = sum(temp) - GSquareByN
tt = y - GSquareByN
te = tt - tc - tr

print('matrix1', matrix1)
print('matrix2', matrix2)
print('n1:', n)
print('n2:', m)
print('\nG: sumOf(matrix[i][j])', G)
print('GSquareByN:', GSquareByN)
print('sumOf(yij**2):', y)
print('tss:', tt)

print('\nt i. **2:', temp)
print('sst(sr**2):', tr)

print('\nt .i **2:', temp2)
print('sst(sc**2):', tc)

print('\nsse(se**2): tss - sr**2 - sc**2:', te)
se = te/((m+n-1))
print('\nse**2: sse(se**2)/(n1+n2-1):', te, '/', m+n-1, ':', se)

fr = tr/(se*(m-1))
fc = tc/(se*(n-1))
print('\nfr: sst(sr**2)/(se**2*(n2-1)):', tr, '/', se*(m-1), ':', fr)
print('fc: sst(sc**2)/(se**2*(n1-1)):', tc, '/', se*(n-1), ':', fc)

print("\nANOVA Table")
print('Variation Source, SS, DF, MSS, VR')
print('Row, Col, Error, total')
print(tr, ',', tc, ',', te, ',', tt)
print(m-1, ',', n-1, ',', (n-1)*(m-1), ',', n*m-1)
print(tr/(m-1), ',', tc/(n-1), ',', te/((n-1)*(m-1)))
print(tr/((m-1)*(te/((n-1)*(m-1)))), ',', tc/((n-1)*(te/((n-1)*(m-1)))))