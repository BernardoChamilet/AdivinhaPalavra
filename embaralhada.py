import random
arq = open("palavras.txt","r")
texto = arq.read()
texto = texto[0:-1]
lista = texto.split(";")
palavra = random.choice(lista)
embaralhada = ""
usadas = []
while len(palavra) > len(embaralhada):
	r = random.randint(0,len(palavra)-1)
	letra = palavra[r]
	if r not in usadas:
		embaralhada = embaralhada + letra
	usadas.append(r)
print(embaralhada)
cont = 0
tentativa = input("Tente advinhar que palavra é essa: ")
while cont < 4 and tentativa != palavra:
	print("Você errou! Tente novamente, você tem mais ",4 - cont," tentativas. ")
	tentativa = input(":")
	cont = cont + 1
if tentativa == palavra:
	print("Parabéns, você acertou!")
else:
	print("Você falhou! A palavra era: ",embaralhada)