
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

# Utilise cette liste pour imprimer des phrases comme
# "I would like to own a Honda motorcycle." pour chaque élément.
def transport():
    trans = ["car", "poney", "plane"]
    for t in trans:
        print(f"I would like to ride a {t}")


    

def main():
    print("\nExercice Name: ")
    name_list = name()
    print("\nExercice Greeting: ")
    greetings(name_list)
    print("\nExercice Transport: ")
    transport()

if __name__ == "__main__":
    main()