#exercice 2

help(list.insert)

liste = ['Alice', 'Bob', 'Tom']
liste.insert(2,'Marc')
print(liste)

#exercice 3

t = []
for i in range(0,10,2):
    t.append(i**2)
print(t)

#exercice 4

t = [0]*10

for i in range(len(t)):
    t[i] = 10 - i
print(t)
