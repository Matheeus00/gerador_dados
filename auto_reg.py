def auto_reg():
    from random import randint
    import numpy as np

    print(r'INSERT INTO locacao (codigo, data_hora_retirada, data_hora_devolucao, situacao, bicicleta_codigo, local_codigo_retirada, local_codigo_devolucao, pessoa_codigo) VALUES')

    situacao = ['devolvida', 'nao devolvida']

    # A data de devolução pode ser de 0 a 5 dias e não pode passar o dia atual


    for i in range(0, 50):
	    intrand = randint(0, 1)
	    randomico = np.random.choice(situacao, 2, replace=False)

	    pessoa = randint(1, 20)
	    local_devl = randint(1, 4)
	    local_retr = randint(1, 4)
	    bicicleta = randint(1, 10)

	    dia_ret = randint(1, 28)
	    mes_ret = randint(1, 5)
	    ano_ret = randint(2018, 2018)

	    dia_dev = randint(1, 28)
	    mes_dev = randint(1, 5)
	    ano_dev = randint(2018, 2018)

	    hora_retirada = randint(7, 18)
	    minuto_retirada = randint(1, 59)

	    hora_devolvida = randint(7, 18)
	    minuto_devolvida = randint(1, 59)


	    if hora_devolvida < hora_retirada:
		    troca = hora_retirada
		    hora_retirada = hora_devolvida
		    hora_devolvida = troca

	    data_ret = f'''{ano_ret}/{mes_ret}/{dia_ret}'''
	    data_dev = f'''{ano_dev}/{mes_dev}/{dia_dev}'''

	    if data_dev > "2018/5/10":
		    situacao[intrand] = 'não_devolvida'
	    else:
		    situacao[intrand] = 'devolvida'
	    
	    if data_dev < data_ret:
		    tt = data_ret
		    data_ret = data_dev
		    data_dev = tt
		    
	    random = f'''(default, '{data_ret} {hora_retirada}:{minuto_retirada}', '{data_dev} {hora_devolvida}:{minuto_devolvida}', '{situacao[intrand]}', {bicicleta}, {local_retr}, {local_devl}, {pessoa}),'''
	    print(random)
