#Capaz de calcular o valor presente, valor futuro, a taxa de juros e o número de períodos a partir dos dados fornecidos
#Legenda: 
#pv -> valor presente, fv-> valor futuro, n-> períodos e i-> taxa de juros.
#pvpmtc-> valor presente a calculado a partir dos fluxos caixa (constantes), taxa de juros e número de períodos
#fvpmtc -> calcula o valor futuro a partir dos dados de fluxo de caixa, taxa de juros e número de períodos
#ipmtc -> calcula a taxa de juros a partir dos dados de fluxo de caixas, valor presente e número de períodos
npmtc -> calcula o número de períodos a partir dos dados de fluxo de caixas, valor presente e taxa de juros

import math

def pvpmtc(pmt, i, n): #sintaxe da calculadora: (fluxo de caixa, taxa de juros, períodos)
    z = (1+i)**n
    y = (z-1)/(i*z)
    pv = pmt*y
    return round(pv, 2)

def fvpmtc(pmt, i, n): #sintaxe: (fluxo de caixa, taxa de juros, períodos)
    z = ((1+i)**n-1)/i
    fv = pmt*z
    return round(fv, 2)

def ipmtc(pmt, pv, n, i_est):
    i = i_est
    while True:
        pv_calc = pvpmtc(pmt, i, n)
        if pv_calc == pv:
            break
        else:
            i = i + 0.0001  # Ajuste fino da taxa de juros
    return round(i, 2)

def n_pmtc(pmt, pv, i):
    n = 1
    while True:
        pv_calc = pvpmtc(pmt, i, n)
        if pv_calc >= pv:
            break
        else:
            n += 1
    return n

# Exemplos de uso:
print("Valor Presente:", pvpmtc(100, 0.1, 20))  #se quiser usar a calculadora, basta trocar os valores dentro da função seguindo a sintaxe: (valor futuro,
print("Valor Futuro:", fvpmtc(100, 0.1, 5))
print("Taxa de Juros:", ipmtc(20, 150, 2, 0.1))
print("Número de Períodos:", n_pmtc(100, 150, 0.1))
