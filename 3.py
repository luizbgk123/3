#3 – Peça para o usuário digitar um número, e mostre para ele se aquele é um número
#primo ou não.

from math import sqrt
n = int(input("Deigite um numero: "))

primo = 0 

if(n > 1):
    for i in range(2, int(sqrt(n)) + 1):
        if  (n % i == 0):
            primo = 1
            break
    if primo == 0:
        print(f"O numero {n} é primo")
    else:
        print(f"O numero {n} não é primo")
else:
        print(f"O numero {n} não é primo")
