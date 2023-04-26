import json
import time
import random

#Discord lista
with open ("discord_lista.txt", "r") as fp:
    discord = json.load(fp)
action = ""

#Sanat siihen, että mitä haluaa tehdä
add = ["lisää", "päivitä", "add"]
remove = ["poista", "remove"]
list = ["lista", "katso"]

#Lisää juttuja
l_nimi = ""
l_discord_nimi = ""

#Poista juttuja
p_nimi = ""

#Alkuun ohjeita
print("-"*20,"\n"
      "Komennot: \n"
      "   Lisää/Päivitä\n"
              "   Poista\n"
              "   Lista\n")
print("-"*20)

while 1==1:                                                 #Looppeja yms, että pysyy kokoajan käynnis
    while action == "":
        action = ""
        action = input("Mitä haluat tehdä: ")
    if action.lower() in add:                               #Jos haluaa lisätä tai päivittää listaa
        print("-"*20)
        print("\n")
        l_nimi = input("Nimi: ")
        l_discord_nimi = input("Discord nimi + tag: ")
        print("\n")
        discord.update({l_nimi.capitalize(): l_discord_nimi})
        print("Lisätään ", l_nimi.capitalize(), " listalle...")
        time.sleep(random.randint(1, 4))
        with open("discord_lista.txt", "w") as fp:
            json.dump(discord, fp)
        print(l_nimi.capitalize(), " lisätty listalle onnistuneesti.")
        time.sleep(random.randint(1, 3))
        print("\n")
        action = ""
        print("-" * 20)
    elif action.lower() in remove:                          #Jos haluaa poistaa listalta
        print("-" * 20)
        print("\n")
        p_nimi = input("Nimi: ")
        print("\n")
        discord.pop(p_nimi.capitalize())
        print("Poistetaan ",p_nimi.capitalize()," listalta...")
        time.sleep(random.randint(1, 4))
        with open("discord_lista.txt", "w") as fp:
            json.dump(discord, fp)
        print(p_nimi.capitalize()," poistettu listalta onnistuneesti.")
        time.sleep(random.randint(1, 3))
        print("\n")
        action = ""
        print("-" * 20)
    elif action.lower() in list:                            #Jos haluaa nähdä listan
        print("-" * 20)
        print("\n")
        for key, value in discord.items():
            print(key.capitalize(), "|", value)
        print("\n")
        action = ""
        print("-" * 20)
    else:                                                   #Antaa ohjeet uudestaan, jos kirjoittaa väärin
        print("-" * 20, "\n"
                        "Komennot: \n"
                        "   Lisää/Päivitä\n"
                        "   Poista\n"
                        "   Lista\n")
        action = ""
        print("-" * 20)
input('Press Enter to Continue')
