# faça um programa que verifique se a pessoa pertence a família "bravi" ou "silva"

sobrenome = input("Entre com o seu nome completo? ")

sobrenome = sobrenome.lower() #coloca todos os elementos da string em lower case

if  "Bravi" in sobrenome or "Silva" in sobrenome:
    print("Você é da família!!")

else:
    print("Você não é da família!")