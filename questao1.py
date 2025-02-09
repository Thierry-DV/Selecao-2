def pertence_fibonacci(numero):
    if numero < 0:
        return False
    a, b = 0, 1
    while a <= numero:
        if a == numero:
            return True
        a, b = b, a + b
    return False

def main():
    try:
        numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    except ValueError:
        print("Por favor, informe um número inteiro válido.")
        return
    
    if pertence_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
