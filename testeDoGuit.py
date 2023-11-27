
import pyttsx3

def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

# Frase desejada
frase = "Oi, eu sou o Batman"

# Chamando a função para falar a frase
falar(frase)
