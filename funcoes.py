import random


# capturando a resposta do usuário e pre-processando
def resposta():
    resp = input('>:')
    resp = resp.lower()
    resp = resp.replace('eh', 'é')
    return resp


def pegaNome(nome):
    if 'o meu nome é ' in nome:
        nome = nome[13:]

    if 'meu nome é ' in nome:
        nome = nome[11:]

    nome = nome.title()
    return nome


def respondeNome(nome):
    conhecidos = ['Hiago', 'Maikon']
    if nome in conhecidos:
        frase = 'Eaew '
    else:
        saudacoes = ['Muito prazer, ', 'Oi, ', 'Olá, ']
        frase = random.choice(saudacoes)

    return frase + nome