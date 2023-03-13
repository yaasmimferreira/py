numero = int(input("Digite um número inteiro: "))

print("Os divisores de", numero, "são:")

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
