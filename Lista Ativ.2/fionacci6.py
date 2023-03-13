num = int(input("Digite um número inteiro (n): "))

fibonacci = [0, 1]

# Loop para gerar os próximos termos da sequência
for i in range(2, num):

    # Cada termo é a soma dos dois termos anteriores
    next_term = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(next_term)


print("Sequência de Fibonacci até o enésimo termo:")
for term in fibonacci:
    print(term)

