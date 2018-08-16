import numpy as np

def cartesian(a,b):
    mat = []
    for x in a:
        v = []
        for y in b:
            v.append(x*y)
        mat.append(v)
    return mat

def complement(a):
    print(1-a)

def max_min(a,b):
    n = len(a)
    m = len(b[0])
    
    mat = []
    
    for i in range(n):
        x = a[i,:]
        t = []
        for j in range(m):
            y = b[:,j]
            t.append(np.amax(np.minimum(x,y)))
        mat.append(t)
    print(np.array(mat))
    
def max_product(a,b):
    n = len(a)
    m = len(b[0])
    
    mat = []
    
    for i in range(n):
        x = a[i,:]
        t = []
        for j in range(m):
            y = b[:,j]
            t.append(np.amax(x*y))
        mat.append(t)
    print(np.array(mat))
    
def containment(a,b):
    mat = a<=b
    print(mat)

def union(a,b):
    mat = np.zeros(a.shape)
    for i in range(len(a)):
        for j in range(len(a[0])):
            mat[i][j]=max(a[i][j],b[i][j])
    print(mat)
    
def intersection(a,b):
    mat = np.zeros(a.shape)
    for i in range(len(a)):
        for j in range(len(a[0])):
            mat[i][j]=min(a[i][j],b[i][j])
    print(mat)

a = [float(x) for x in input().split(" ")]
b = [float(x) for x in input().split(" ")]
c = [float(x) for x in input().split(" ")]

mat1 = np.array(cartesian(a,b))
mat2 = np.array(cartesian(b,c))

print("\nRelation R")
for i in mat1:
    print(i)

print("\nRelation S")
for i in mat2:
    print(i)

inp = int(input("1.Complement R\n2.Complement S\n3.MAX-PRODUCT\n4.MAX-MIN\n5.Containment\n6.Union\n7.Intersection\n"))

while inp>0:
    if inp==1:
        print("Complement R\n")
        complement(mat1)
    elif inp==2:
        print("Complement S\n")
        complement(mat2)
    elif inp==3:
        print("MAX PRODUCT\n")
        max_product(mat1,mat2)
    elif inp==4:
        print("MAX-MIN\n")
        max_min(mat1,mat2)
    elif inp==5:
        print("Containment\n")
        containment(mat1,mat2)
    elif inp==6:
        print("Union\n")
        union(mat1,mat2.T)
    else:
        print("Intersection\n")
        intersection(mat1,mat2)
    inp = int(input())