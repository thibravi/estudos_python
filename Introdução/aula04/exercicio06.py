# loteria. usuário tentando adivinhar um número V2
# for

numero_sorte = 7


for i in range(3):

    numero = int(input("Entre com um número entre 1 e 15: "))

    if numero == numero_sorte:
        print("Você acertou!")
        break

    elif numero > numero_sorte:
        print("Você errou! Tente um número menor.")

    else:
        print("Você errou! Tente um número maior.")