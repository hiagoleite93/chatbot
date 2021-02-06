import random
import json
import sys
import os
import subprocess as s


class Chatbot():
    def __init__(self, nome):
        try:
            memoria = open(nome + '.json', 'r')
        except FileNotFoundError:
            memoria = open(nome + '.json', 'w')
            memoria.write('["Hiago", "Maikon"]')
            memoria.close()
            memoria = open(nome + '.json', 'r')
        self.nome = nome
        self.conhecidos = json.load(memoria)
        memoria.close()
        self.historico = []
        self.frases = {'oi': 'Olá, qual o seu nome?', 'olá': 'Olá, qual o seu nome?', 'tchau': 'Até logo'}

    def escuta(self):
        frase = input('>:')
        frase = frase.lower()
        frase = frase.replace('eh', 'é')
        return frase

    def pensa(self, frase):
        if frase in self.frases:
            return self.frases[frase]
        if frase == 'aprende':
            chave = input('Digite a frase: ')
            resp = input('Digite a resposta: ')
            self.frases[chave] = resp
            return 'Aprendido'

        if self.historico[-1] == 'Olá, qual o seu nome?':
            nome = self.pegaNome(frase)
            resp = self.respondeNome(nome)
            return resp
        try:
            resp = str(eval(frase))
            return resp
        except:
            pass
        return 'Não entendi'

    def pegaNome(self, nome):
        if 'o meu nome é ' in nome:
            nome = nome[13:]

        if 'meu nome é ' in nome:
            nome = nome[11:]

        nome = nome.title()
        return nome

    def respondeNome(self, nome):
        conhecidos = ['Hiago', 'Maikon']
        if nome in self.conhecidos:
            frase = 'Eaew '
        else:
            saudacoes = ['Muito prazer, ', 'Oi, ', 'Olá, ']
            frase = random.choice(saudacoes)
            self.conhecidos.append(nome)
            memoria = open(self.nome + '.json', 'w')
            json.dump(self.conhecidos, memoria)
            memoria.close()

        return frase + nome

    def fala(self, frase):
        if 'executa ' in frase:
            plataforma = sys.platform
            comando = frase.replace('executa ', '')
            if 'win' in plataforma:
                os.startfile(comando)
            try:
                if 'linux' in plataforma:
                    s.Popen(comando)
            except FileNotFoundError:
                s.Popen(['xdg-open', comando])
        else:
            print(frase)
        self.historico.append(frase)
        memoria = open(self.nome+'.json', 'w')
        json.dump(self.conhecidos, memoria)
        memoria.close()