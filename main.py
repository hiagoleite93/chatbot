from funcoes import *
from chatbot import Chatbot

Bot = Chatbot('Edu')
while True:
    frase = Bot.escuta()
    resp = Bot.pensa(frase)
    Bot.fala(resp)
    if resp == 'tchau':
        break
