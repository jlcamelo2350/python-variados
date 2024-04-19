#Calculadora de arranjo e combinação simples. Não tem muito oq dizer aq

def calcular_combinacao_simples(n, p):
    i = 1
    j = 1
    p_fat = p
    q = p
    p = n - p
    n_fat = n
    pn_fat = p

    while i < n:  ###nesse primeiro while calcularei n!
        n_fat = n_fat * i
        i += 1
        while j < q:  ###nesse while calcularei p!
            p_fat *= j
            j += 1
        if pn_fat != 1:  ##agora, calculo (n-p)!
            while j < p:
                pn_fat *= j
                j += 1
        else:
            pn_fat = 1
    A = p_fat * pn_fat  ## aqui calculo p!*(n-p)!
    combinacao_s = n_fat / (p_fat * pn_fat)

    print(f'{n_fat} é valor de n!')
    print(f'{p_fat} é valor de p!')
    print(f'{pn_fat} é valor de (n-p)!')
    print(f'{A} é valor de p!*(n-p)!')
    print(f'{combinacao_s} é o valor da combinação simples')


def calcular_arranjo_simples(m, p):
    i = 1
    j = 1
    pm = m - p
    m_fat = m
    pm_fat = pm

    while i < m:
        m_fat = m_fat * i  # Calcula o fatorial de m, m!, fazendo n*1, depois (m*1)*2, depois (m*1*2)*3... até m-1
        i += 1
        if pm_fat != 1:
            while j < pm:
                pm_fat *= j  # Calcula o fatorial de p, p!
                j += 1
        else:
            pm_fat = 1  # Calcula o fatorial (m-p)!
    arranjo_s = (m_fat) / (pm_fat)  # Nda mais é do que m!/(m-p)!, que é como se calcula arranjo simples
    print(arranjo_s)


def main():
    print("Escolha o que deseja calcular:")
    print("1. Combinação simples")
    print("2. Arranjo simples")
    escolha = input("Digite 1 ou 2: ")

    if escolha == "1":
        n = int(input('Digite o valor de n: '))
        p = int(input('Digite o valor de p: '))
        print('Como a posição NÃO importa, então utilizaremos combinação simples.')
        print('Combinação simples, tem fórmula (n!)/(p!*(n-p)!)')
        calcular_combinacao_simples(n, p)
    elif escolha == "2":
        m = int(input('Digite o valor de m: '))
        p = int(input('Digite o valor de p: '))
        print('Arranjo simples tem fórmula: (m!)/(m-p)!')
        calcular_arranjo_simples(m, p)
    else:
        print("Escolha inválida")


if __name__ == "__main__":
    main()