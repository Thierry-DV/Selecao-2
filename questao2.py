def contar_letra_a(s):
    return s.lower().count('a')

def main():
    s = input("string para verificar a quantidade de letras 'a': ")
    
    quantidade_a = contar_letra_a(s)
    
    if quantidade_a > 0:
        print(f"A letra 'a' aparece {quantidade_a} vez(es) na string.")
    else:
        print("A letra 'a' não aparece na string.")

if __name__ == "__main__":
    main()
