import random

numeros=int(input("Digite um numero: "))

print("O número da loteria é: ")

if numeros == 6:
        for numeros in range(6):
            aleatorios = (random.randrange(1, 100))
            print( aleatorios, end=" ")
elif numeros == 10:
        for numeros in range(10):
            aleatorios = (random.randrange(1, 100))
            print( aleatorios, end=" ")
elif numeros == 16:
        for numeros in range(16):
            aleatorios = (random.randrange(1, 100))
            print(aleatorios, end=" ")
else:
    print("Digite um sorteio válido!")


