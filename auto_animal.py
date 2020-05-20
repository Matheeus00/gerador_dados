def auto_animal():
    import random
    import numpy as np
    import datetime


    nomes = ['Aya', 'Axel', 'Ace', 'Aron', 'Alcapone', 'Biba', 'Babalu', 
    'Billy', 'Belinha', 'Doug', 'Dudu', 'Dunga', 'Dol', 'Ed', 'Eloy', 'Elvis',
    'Enzo', 'Lupi', 'Nina', 'Tufão'] 

    intrand = random.randint(0, 19)
    randomico = np.random.choice(nomes, 20, replace=False)

    randia = random.randint(1, 31)
    randmes = random.randint(1, 12)
    randano = random.randint(2010, 2019) 
    data_nascimento = f'{randano}/{randmes}/{randia}'

    id_port = random.randint(1, 3)
    id_raca = random.randint(1, 5)

    random = f'''(default, '{randomico[intrand]}', '{data_nascimento}', {id_port}, {id_raca}),'''
    print(random)
