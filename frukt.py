import random 


def print_fruit(userinput):
    fnr = int(userinput)
    print("\n" + frukter[fnr-1] + " kommer här!")


frukter =("Apelsin", "Mango", "Äpple", "Banan", "Päron", "Dragonfrukt", "Kiwi", "Persika", "Blåbär")

looping = True

while looping:

    print("================================================================")
    print("\n FruktAutomat V0.2 \n")
    print("================================================================")

    i = 1

    for frukt in frukter:
        print(str(i) + ": " + frukt)
        i += 1



    frukter = input("\n Siffra --->:")



    go = input("\n Vill du välja en frukt till? j/n \n")

    if (go == "n"):
        break


print("================================================================")

print("Föresten här får du en till frukt")
slumpfrukt = random.randint(0, 5)
print_fruit(slumpfrukt)