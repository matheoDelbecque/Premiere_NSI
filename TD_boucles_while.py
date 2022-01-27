#exercice 2
#1)
n = 0
while n < 10 :
    print(n)
    n = n + 2
#2)
n = 61
while n < 100 :
    print(n)
    n = n + 2
    
#exercice 3
#1)
def decroissant_for(n):
    for i in range(n,-1,-1):
        print(i, end=' ')
decroissant_for(6)
#2)
def decroissant_while(n):
    while n > -1 :
        print(n,end=' ')
        n = n - 1
decroissant_while(6)

#exercice 4
#3)
def somme1(n1,n2):
    S = 0
    for k in range(n1,n2):
        S = S + k
    return S
print(somme1(1,5))

def somme2(n1,n2):
    S = 0
    for k in range(n2):
        k = k + 1
        S = S + k
    return S
print(somme2(1,5))
