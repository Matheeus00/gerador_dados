from auto_acompanhamento import auto_acompanhamento
from auto_animal import auto_animal
from auto_reg import auto_reg

print('1 - auto_acompanhamento')
print('2 - auto_animal')
print('3 - auto_reg')

opcao = int(input('Qual módulo você quer usar? '))

if opcao == 1:
    auto_acompanhamento()
elif opcao == 2:
    auto_animal()
elif opcao == 3:
    auto_reg()
elif opcao < 1 or opcao > 3:
    print('Digite um número válido')
    print('1, 2 ou 3.')
