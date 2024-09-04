# Sequência a) 1, 3, 5, 7, ___
sequencia_a = [1, 3, 5, 7]
proximo_elemento_a = sequencia_a[-1] + 2

# Sequência b) 2, 4, 8, 16, 32, 64, ____
sequencia_b = [2, 4, 8, 16, 32, 64]
proximo_elemento_b = sequencia_b[-1] * 2

# Sequência c) 0, 1, 4, 9, 16, 25, 36, ____
sequencia_c = [0, 1, 4, 9, 16, 25, 36]
proximo_elemento_c = (len(sequencia_c))**2

# Sequência d) 4, 16, 36, 64, ____
sequencia_d = [4, 16, 36, 64]
proximo_elemento_d = ((len(sequencia_d) + 1) * 2)**2

# Sequência e) 1, 1, 2, 3, 5, 8, ____
def fibonacci(n):
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

sequencia_e = [1, 1, 2, 3, 5, 8]
proximo_elemento_e = fibonacci(len(sequencia_e) + 1)

# Sequência f) 2, 10, 12, 16, 17, 18, 19, ____
sequencia_f = [2, 10, 12, 16, 17, 18, 19]
proximo_elemento_f = sequencia_f[-1] + 1

print(f"Próximo elemento da sequência a: {proximo_elemento_a}")
print(f"Próximo elemento da sequência b: {proximo_elemento_b}")
print(f"Próximo elemento da sequência c: {proximo_elemento_c}")
print(f"Próximo elemento da sequência d: {proximo_elemento_d}")
print(f"Próximo elemento da sequência e: {proximo_elemento_e}")
print(f"Próximo elemento da sequência f: {proximo_elemento_f}") 
