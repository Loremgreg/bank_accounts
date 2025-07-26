
# Stocke les noms de quelques amis dans une liste appelée 'names'.
# Affiche chaque nom un par un en accédant à chaque élément de la liste.
def name():
    names = ["Sara", "Bob", "Jack"]
    for n in names:
        print(n)
    return names

# À partir de la liste 'names' de l'exercice 3-1, imprime un message personnalisé
def greetings(names):
    for n in names:
        print(f"Hello {n}!")


def transport():
    trans = ["car", "poney", "plane"]
    for t in trans:
        print(f"I would like to ride a {t}")

def exercise_3_4():
    guest = ["Albert", "Seneque", "Ciceron"]
    for g in guest:
        print(f"Hi {g}, pass by when you free")
    return guest
# À partir de l'exercice 3-4, annonce qu'un invité ne peut plus venir,
# remplace ce nom, puis imprime à nouveau les invitations.
def exercise_3_5(guest):
        print(f"{guest[0]} cannot come")
        guest[0] = "Copernic"
        for g in guest:
            print(f"Hi {g}, see you tonight")
        return guest
# Exo 3-6. More Guests:
# Tu as trouvé une grande table, ajoute trois nouveaux invités :
# - insert() au début,
# - insert() au milieu,
# - append() à la fin,
# puis imprime les invitations mises à jour.

def exercise_3_6(guest):
        for g in guest:
            print(f"Hi {g}, I found a bigger table")
        guest.insert(0, "Jonhy")
        middle_list = len(guest)//2
        guest.insert(middle_list, "Clara")
        guest.append("Popol")
        for g in guest:
            print(f"Hi {g}, I'll see you tonight!")

# Exo 3-7. Shrinking Guest List:
# Maintenant, tu ne peux inviter que deux personnes :
# - Informe qu'il ne reste que deux places,
# - pop() un à un les invités excédentaires en t'excusant,
# - informe les deux derniers qu'ils sont toujours invités,
# - supprime la liste et affiche-la vide.

def exercise_3_7():
    # TODO: utilise pop() et del pour ramener la liste à vide
    pass

    

def main():
    print("\nExercice Name: ")
    name_list = name()

    print("\nExercice Greeting: ")
    greetings(name_list)

    print("\nExercice Transport: ")
    transport()

    print("\nExercice 3-4:")
    guest_list = exercise_3_4()

    print("\nExercice 3-5:")
    new_guest_list = exercise_3_5(guest_list)

    print("\nExercice 3-6:")
    exercise_3_6(new_guest_list)

    print("\nExercice 3-7:")
    exercise_3_7()

if __name__ == "__main__":
    main()