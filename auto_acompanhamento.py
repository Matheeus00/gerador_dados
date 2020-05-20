def auto_acompanhamento():
    from random import randint
    import numpy as np


    servicos = ['banho', 'tosa', 'vacinacao', 'consulta', 'banho e tosa']

    print(r'INSERT INTO acompanhamento (codigo, data, descricao, quantidade, valor_gasto, animal_codigo) VALUES')

    for i in range(1, 50):
	    intrand = randint(0, 4)
	    randomico = np.random.choice(servicos, 5, replace=False)
	    quant = randint(1, 3)

	    valor_servico = 0
	    if servicos[intrand] == 'banho':
		    valor_servico = 50
	    if servicos[intrand] == 'tosa':
		    valor_servico = 15
	    if servicos[intrand] == 'vacinacao':
		    valor_servico = 40
	    if servicos[intrand] == 'consulta':
		    valor_servico = 60
	    if servicos[intrand] == 'banho e tosa':
		    valor_servico = 65

	    random = f'''(default, '{randint(2020, 2020)}/{randint(1, 5)}/{randint(1, 10)}', {randomico[intrand]}, {quant}, {valor_servico*quant}, {randint(1, 20)}),'''

	    print(random)
