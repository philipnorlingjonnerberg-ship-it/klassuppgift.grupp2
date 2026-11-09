ord = "python"
gissade_bokstaver = []
fel_gissningar = []

while True:
    print("\nOrdet:", end=" ")

    for bokstav in ord:
        if bokstav in gissade_bokstaver:
            print(bokstav, end=" ")
        else:
            print("*", end=" ")

    print("\nFel gissningar:", fel_gissningar)

    gissning = input("\nGissa en bokstav: ").lower()

    if gissning in gissade_bokstaver or gissning in fel_gissningar:
        print("Du har redan gissat den bokstaven!")
        continue

    if gissning in ord:
        print("Rätt gissat!")
        gissade_bokstaver.append(gissning)
    else:
        print("Fel gissat!")
        fel_gissningar.append(gissning)

    if all(bokstav in gissade_bokstaver for bokstav in ord):
        print("\nGrattis! Du gissade rätt ord:", ord)
        break
