def get_even_numbers(numbers):
    """
    Retourne une nouvelle liste contenant uniquement les entiers pairs de 'numbers'.
    """
    new_list = []
    for n in numbers:
        if n % 2 == 0:
            new_list.append(n)
    return new_list



def main():
    sample = [1, 2, 3, 4, 5, 6]
    evens = get_even_numbers(sample)
    print("Nombres pairs:", evens)

if __name__ == "__main__":
    main()

