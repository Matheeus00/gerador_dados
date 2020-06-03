import random
import time

print('''INSERT INTO ponto (idponto, dataponto, horaponto, codfunc, codlocal, tiporegistro)
VALUES''')

mes = '05'
ano = '2020'
dias = ['01', '04', '05', '06', '07', '08', '11', '12', '13', '14', '15', '18', '19', '20', '21', '22', '25', '26', '27', '28', '29']
hora = ['08:00', '12:00', '13:00', '17:00']


def ti():
    for i in range(0, len(dias)):
        for a in range(0, len(hora)):
            print(f"(default, '{dias[i]}/{mes}/{ano}', '{hora[a]}', 1, 1, 'eletronico'),")


def rh():
    for i in range(0, len(dias)):
        for a in range(0, len(hora)):
            print(f"(default, '{dias[i]}/{mes}/{ano}', '{hora[a]}', 2, 1, 'eletronico'),")


def fin():
    for i in range(0, len(dias)):
        for a in range(0, len(hora)):
            print(f"(default, '{dias[i]}/{mes}/{ano}', '{hora[a]}', 3, 1, 'eletronico'),")


def cont():
    for i in range(0, len(dias)):
        for a in range(0, len(hora)):
            print(f"(default, '{dias[i]}/{mes}/{ano}', '{hora[a]}', 4, 1, 'eletronico'),")


def com():
    for i in range(0, len(dias)):
        for a in range(0, len(hora)):
            randomico = random.randint(1, 3)
            trabalho = 'eletronico'

            if randomico == 2:
                randomico = 3
                trabalho = 'digital'
            
            print(f"(default, '{dias[i]}/{mes}/{ano}', '{hora[a]}', 5, {randomico}, '{trabalho}'),")

ti()
rh()
fin()
cont()
com()