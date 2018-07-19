# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a = [x for x in input().split(" ")]
b = [x for x in input().split(" ")]
d_a = {}
d_b = {}
for x in a:
    x = x.split(',')
    d_a[int(x[0])]=float(x[1])

for x in b:
    x = x.split(',')
    d_b[int(x[0])]=float(x[1])

print("set A "+str(d_a))
print("set B "+str(d_b))

un = d_a.copy()

for x in un.keys():
    if x in d_b.keys():
        un[x]=max(un[x],d_b[x])
    
print("union "+str(un))

inter = {}

for x in d_a.keys():
    inter[x]=min(d_a[x],d_b[x])
        
print("intersection "+str(inter))

a_comp = {}
for x in d_a.keys():
    a_comp[x]=(1.0-d_a[x])
print("A complement "+str(a_comp))

b_comp = {}
for x in d_b.keys():
    b_comp[x]=(1.0-d_b[x])
print("B complement "+str(b_comp))
