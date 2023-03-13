import random 

def print_fruit(userinput):
    fnr = int(userinput)
    print("\n" + frukter[fnr-1] + " kommer här!")

    

frukter =("Apelsin", "Mango", "Äpple", "Banan", "Päron", "Dragonfrukt", "Kiwi", "Persika", "Blåbär")

looping = True

while looping:

    go = input("\n Vill du välja en frukt till? \n")

    if (go == "n"):
        break
