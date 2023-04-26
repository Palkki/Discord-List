import json
import time
import random

#Discord list
with open ("discord_list.txt", "r") as fp:
    discord = json.load(fp)
action = ""

#Actions
add = ["add", "update"]
remove = ["remove", "delete"]
list = ["list", "watch", "show"]

#add stuff
add_name = ""
add_discord_name = ""

#Remove stuff
del_name = ""

#Guide / Commands
print("-"*20,"\n"
      "Commands: \n"
      "   Add/Update\n"
              "   Remove\n"
              "   List\n")
print("-"*20)

while 1==1:                                                 #Loops etc.
    
    while action == "":
        action = ""
        action = input("What would you like to do: ")
        
    if action.lower() in add:                               #If  you want to add to the list
        print("-"*20)
        print("\n")
        add_name = input("Name: ")
        add_discord_name = input("Discord name + tag: ")
        print("\n")
        discord.update({add_name.capitalize(): add_discord_name})
        print("Adding ", l_nimi.capitalize(), " to the list...")
        time.sleep(random.randint(1, 4))
        with open("discord_list.txt", "w") as fp:
            json.dump(discord, fp)
        print(add_name.capitalize(), " added to the list succesfully.")
        time.sleep(random.randint(1, 3))
        print("\n")
        action = ""
        print("-" * 20)
        
    elif action.lower() in remove:                          #If you want to remove from the list
        print("-" * 20)
        print("\n")
        del_name = input("Name: ")
        print("\n")
        discord.pop(del_name.capitalize())
        print("Deleting ",del_name.capitalize()," from the list...")
        time.sleep(random.randint(1, 4))
        with open("discord_list.txt", "w") as fp:
            json.dump(discord, fp)
        print(del_name.capitalize()," succesfully deleted from the list.")
        time.sleep(random.randint(1, 3))
        print("\n")
        action = ""
        print("-" * 20)
        
    elif action.lower() in list:                            #If you want to see the list
        print("-" * 20)
        print("\n")
        for key, value in discord.items():
            print(key.capitalize(), "|", value)
        print("\n")
        action = ""
        print("-" * 20)
        
    else:                                                   #Gives the guide again, if you misspell
        print("-" * 20, "\n"
                        "Commands: \n"
                        "   Add/Update\n"
                        "   Remove\n"
                        "   List\n")
        action = ""
        print("-" * 20)
