import random
import time

print('''INSERT INTO resumodiario (codfunc, datares, minutos)
VALUES''')

mes = '05'
ano = '2020'
dias = ['01', '04', '05', '06', '07', '08', '11', '12', '13', '14', '15', '18', '19', '20', '21', '22', '25', '26', '27', '28', '29']


funcionarios = [1, 2, 3, 4, 5]


for i in range(0, len(dias)):
    for a in range(0, len(funcionarios)):
        ran = random.randint(0, 10)
        print(f"({funcionarios[a]}, '{dias[i]}/{mes}/{ano}', '{ran}'),")