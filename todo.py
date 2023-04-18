import sys


LISTE=[]
pseudo = input("Laissez moi mettre un pseudo sur votre visage ? :")

PRESENTATION = f"Bienvenue sur votre assistants virtuel todo 😋 {pseudo}".capitalize()

MENU =f"""
1.✔  Ajouter une tache
2.😒 Suppimer une tache
3.😃 Afficher toute les taches
4.🧺 Vider la Todo
5.quitter
👉Votre choix:"""

MENU_CHOIX =["1","2","3","4","5"]


while True:
    print(PRESENTATION)
    print(MENU)
    user_choice =""
    while user_choice not in MENU_CHOIX:
        user_choice = input(f"Faites un choix entre  1 et 5 svp {pseudo} ! ... : ")
        if user_choice not in MENU_CHOIX:
            print("entrez une valeur comprise entre 1 et 5 svp !...".upper())
    if user_choice =="1":
        task = input("Entrez la novelle tache dans la todo : ")
        if task not in LISTE:
            LISTE.append(task)
            print(f"La tache {task} a bien été ajouter 😋")
        else:
            print(f"Cette tache {task} existe deja dans cette todo! 🙄")
    elif user_choice=="2":
        task = input("Entrez le nom de la tache a supprimer de la todo : ")
        if task in LISTE:
            LISTE.remove(task)
            print(f"Cette tache {task} a été supprimer avec succes!😁 {pseudo}")
        else:
            print(f"Cette tache {task} n'existe pas dans cette liste!🙄 {pseudo}")
    elif user_choice=="3":
        if LISTE:
            print(f" {pseudo} voila le contenue de votre todo 🤗")
            for i , task in enumerate(LISTE,1):
                print(f"{i}. {task}")
        else:
            print("Aucune tache dans votre todo🥱")
    elif user_choice=="4":
        question = input(f"Voulez vous vraiment vider votre todo ? : oui(o) ou non(n) {pseudo} : ")
        if question=="o":
            LISTE.clear()
            print(f"Votre todo a  bien été nettoyer🤗 {pseudo} ")
        else:
            print(f"Il semble que c'était une erreur  {pseudo}")
    elif user_choice=="5":
        print("Merci et Aurevoir ! ")
        sys.exit()
    print("="*100)







