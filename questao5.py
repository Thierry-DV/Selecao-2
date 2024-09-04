def identificar_interruptores():
    # Estado inicial: todos os interruptores estão desligados.
    
    # Passo 1: Ligue o interruptor 1 e espere por alguns minutos.
    interruptor_1 = 'ligado'
    print("Ligue o interruptor 1 e espere alguns minutos.")
    
    # Passo 2: Desligue o interruptor 1 e ligue o interruptor 2.
    interruptor_1 = 'desligado'
    interruptor_2 = 'ligado'
    print("Desligue o interruptor 1 e ligue o interruptor 2.")
    
    # Passo 3: Vá até a sala das lâmpadas para a primeira verificação.
    print("Vá até a sala das lâmpadas.")
    
    # Possibilidades ao verificar as lâmpadas:
    # Lâmpada A: se estiver acesa e quente, é controlada pelo interruptor 1.
    # Lâmpada B: se estiver acesa e fria, é controlada pelo interruptor 2.
    # Lâmpada C: se estiver apagada, é controlada pelo interruptor 3.
    
    print("""
    - Se encontrar uma lâmpada acesa e quente, ela é controlada pelo interruptor 1.
    - Se encontrar uma lâmpada acesa e fria, ela é controlada pelo interruptor 2.
    - Se encontrar uma lâmpada apagada, ela é controlada pelo interruptor 3.
    """)

    # Fim do processo. Com base nessas observações, você pode identificar qual interruptor controla qual lâmpada.
    
# Executa o procedimento
identificar_interruptores()
