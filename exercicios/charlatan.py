#!/usr/bin/env python3

# charlatan.py
# charlatan crea un ficheiro de texto con palabras pseudoaleatorias que se toman 
# dunha lista que pode definir o programador
#
# Pode definirse o numero de palabras para crear un ficheiro mais grande

import random

ficheiro = open("dataset.txt","a") 
PsudoRandomWords = ["Saraiba ", "Pachuzo ", "Chorima ", "Moraima ", "Luscofusco ", "Licorka ", "Fume "]

index = 0
# Incrementa o rango para facer o ficheiro mais grande
#15000000 -> 112MB
#30000000 -> 223MB

numero_palabras = 15000000

for x in range(numero_palabras):
   #Cambia o end range se modificas o numero de randomWords
   index = random.randint(0,6)
   ficheiro.write(PsudoRandomWords[index])
   if x % 20 == 0:
      ficheiro.write('\n')