numero = int(input("Digite o número a ser buscado: "))

n1 = 0
n2 = 1

while True:
    if numero == n1:
        print("O número pertence a sequência de Fibonacci")
        break

    elif numero < n1:
        print("O número não pertence a sequência de Fibonacci")
        break
    
    n1, n2 = n2, n1+n2

    
