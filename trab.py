import requests
import json

print('peso até 1 KG, para o estado PR: R$ 10,00 , outros estados: R$12,50 \npeso de 1,1 até 5,0 KG, para o estado PR: R$15,00 , outros estados: R$19,90 \npeso de 5,1 até 10,0 KG, para o estado PR: R$22,50 , outros estados: R$29,90 \npeso acima de 10 KG, para o estado PR: R$37,50 , outros estados: R$49,90')

cep = input('\nDigite seu cep para calcular o valor do frete(8 digitos, somente numeros): ')
peso = input('Digite o peso da sua carga para o calculo do frete(em KG): ')

#verificação se o cep contem 8 digitos e apenas numeros
while len(cep) !=8 and cep.isdecimal():
    print('O cep deve conter 8 digitos e apenas numeros')
    cep = input('Digite novamente: ')
else:
    print('Cep valido')

#link para consumir a API
link =f'https://viacep.com.br/ws/{cep}/json/'
localidade = requests.get(link)
#conversao para modelo json
localidade = localidade.json()
#UF do cep solicitado
localidade_UF = localidade['uf']
print(localidade_UF)







