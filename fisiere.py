# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 14:27:10 2021

@author: Durnea Maxim
"""
with open("fisier1.txt","w")as f:
    x=input("dati sirul de caractere: ")
    f.write(x)
with open('fisier1.txt',"r")as f1:
    caract=f1.read()
vocale=['a','e','i','o','u']
vocale_lista=[]
numar=0
for i in caract:
    if i.isalpha():
        if i.lower()in vocale:
            vocale_lista.append(i)
            numar+=1
with open('fisier.txt','w')as f2:
    for litera in vocale_lista:
        f2.write(f"{litera};")
    f2.write(f'\nsunt:{numar} caractere')