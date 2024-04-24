import requests
import json
import datetime

agora = datetime.datetime.now()
dataFormatada = agora.strftime('%d/%m/%Y %H:%M')

print('peso até 1 KG, para o estado PR: R$ 10,00 , outros estados: R$12,50 \npeso de 1,1 até 5,0 KG, para o estado PR: R$15,00 , outros estados: R$19,90 \npeso de 5,1 até 10,0 KG, para o estado PR: R$22,50 , outros estados: R$29,90 \npeso acima de 10 KG, para o estado PR: R$37,50 , outros estados: R$49,90')

cpf = input('\nDigite o CPF do cliente: ')
cep = input('Digite seu cep para calcular o valor do frete(8 digitos, somente numeros): ')
peso = float(input('Digite o peso da sua carga para o calculo do frete(em KG): '))

while len(cpf) != 11 and cpf.isdecimal():
    print('O cpf deve conter 11 digitos e apenas numeros')
    cpf = input('Digite novamente: ')

#verificação se o cep contem 8 digitos e apenas numeros
while len(cep) != 8 and cep.isdecimal():
    print('O cep deve conter 8 digitos e apenas numeros')
    cep = input('Digite novamente: ')

#link para consumir a API
link = f'https://viacep.com.br/ws/{cep}/json/'
localidade = requests.get(link)
#conversao para modelo json
localidade = localidade.json()
#UF do cep solicitado
localidade_UF = localidade['uf']


#print(localidade_UF)

def calcular_frete(peso, localidade_UF):
    if peso <= 1.0:
        frete = 10.00 if localidade_UF == "PR" else 12.50
    elif peso <= 5.0:
        frete = 15.00 if localidade_UF == "PR" else 19.90
    elif peso <= 10.0:
        frete = 22.50 if localidade_UF == "PR" else 29.90
    elif peso > 10.0:
        frete = 37.50 if localidade_UF == "PR" else 49.90
    return frete


frete = float( calcular_frete(peso, localidade_UF))
frete_str = f"{frete:.2f}".replace('.', ',')
print(f'o valor do frete sera de {frete_str}. Data da compra: {dataFormatada}')
