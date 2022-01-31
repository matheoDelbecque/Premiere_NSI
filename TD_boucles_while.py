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
    for k in range(n1+1,n2+1):
        S = S + k
    return S
print(somme2(1,5))

#exercice 5
#1)
def nombres_alenvers(n):
    alenvers = ''
    while n > 0:
        alenvers = alenvers + str(n%10)
        n = n // 10
    return int(alenvers)
print(nombres_alenvers(1234))

#2)
def palindrome(n):
    return n == nombres_alenvers(n)
print(palindrome(1234))
print(palindrome(121))

#exercice 8
def est_present(c,s):
    i = 0
    while i < len(s):
        res = c == s[i]
        i = i + 1
        if res == True:
            return res
    return False
print(est_present('t','python'))
print(est_present('z',"je ne trouve pas"))
print(est_present('a',''))
