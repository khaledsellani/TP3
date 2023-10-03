# Le jeu de role 
# TP universitaire Python

import random
import sys

points_vie_ennemi = 50
mes_points_de_vie = 50

mes_potions = 3 

msg = "Souhaitez vous attaquez (1) ou utilisez une potion (2) ? "
choice = input(msg)

while True:
    while choice.isdigit() == False:
        choice = input(msg)

    while int(choice) not in [1,2]:
        choice = input(msg)

    if int(choice) == 1:
        mon_attaque = random.randint(5,10)
        attaque_ennemi = random.randint(5,15)

        mes_points_de_vie -= attaque_ennemi
        points_vie_ennemi -= mon_attaque

        if mes_points_de_vie <= 0:
            print("     l'ennemi a gagne !".upper())
            sys.exit()
        if points_vie_ennemi <= 0:
            print("     vous avez gagne !".upper())
            sys.exit()

        new_msg = f"""Vous avez inflige {mon_attaque} points de degats a l'ennemi.
l'ennemi Vous a inflige {attaque_ennemi} points de degats.
il vous reste {mes_points_de_vie} points de vie.
il reste {points_vie_ennemi} points de vie a l'ennemi.
                   """
        print(new_msg)
        print("-"*30)
        choice = input(msg)
    else:
        if mes_potions >= 1:
            mes_potions -= 1

            for i in range(2):
                if i==1:
                    print("Vous passez le tour ...")

                attaque_ennemi = random.randint(5,15)

                if i==0:
                    aleatoire = random.randint(15,50)
                    mes_points_de_vie += aleatoire

                mes_points_de_vie -= attaque_ennemi
                
                if mes_points_de_vie <= 0:
                    print("     l'ennemi a gagne !".upper())
                    sys.exit()

                if i==0:
                    msg1 = f""" Vous recuperez {aleatoire} points de vie ( il vous reste {mes_potions} potions )
L'ennemi vous a inflige {attaque_ennemi} points de degats
il vous reste {mes_points_de_vie} points de vie.
il reste {points_vie_ennemi} points de vie a l'ennemi.
                            """
                    print(msg1)
                else:
                    msg1 = f"""L'ennemi vous a inflige {attaque_ennemi} points de degats
il vous reste {mes_points_de_vie} points de vie.
il reste {points_vie_ennemi} points de vie a l'ennemi.
                            """
                    print(msg1)
                print("-"*30)
                if i==1:
                    choice = input(msg)
        else:
            print("il vous reste rien de potions. ")
            choice = input(msg)




