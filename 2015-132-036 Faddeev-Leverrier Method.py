'''
Rajiv Das
2015 132 036
This programm calculates Inverse of 3x3 Input matrix and its determinant by "Faddeev-Leverrier Method"
The equations were taken from "An Introduction to Computational Physics - TAO PANG"
'''
A=[]#The input matrix
I = []


print("Input a 3X3 matrix:")

for i in range (3):#Loop for input matrix
    a=[]
    for j in range (3):
        a.append(float(input(">>>")))
    A.append(a)

for i in range(3):#Loop for identity matrix
    b = []
    for j in range(3):
        if i==j:
            b.append(1)
        else:
            b.append(0)
    I.append(b)

B = []
p = []
B.insert(0,A)
for n in range (3): #Loop for calculating determinant and inverse .
    S = 0
    X = []
    for i in range(3):#Loop for coefficents Cn

        for j in range(3):
            if i == j:
                S = (S + B[n][i][j])
    c=S/(n+1)
    p.append(c)
    for i in range(3):
        for j in range(3):
            Z=[]
            for cc in range (3):
                q=[]
                for ccc in range (3):
                    Y = B[n][cc][ccc] - p[n] * I[cc][ccc]
                    q.append(Y)
                Z.append(q)
            for a in range(3):
                row = []
                for aa in range(3):
                    s = 0
                    for aaa in range(3):
                        s = s + A[a][aaa] * Z[aaa][aa]
                    row.append(s)
                X.append(row)
    B.insert(n+1,X)

print("Determinant is {}".format(p[2]))

INV=[]
for i in range (3):#Loop for inverse matrix
    y=[]
    for j in range (3):
        x=((B[1][i][j])-((p[1])*(I[i][j])))/(p[2])
        y.append(x)
    INV.append(y)
for i in range (3):
    for j in range (3):
        print(INV[i][j], end=" ")
    print()