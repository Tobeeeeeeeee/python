vokaler = "aeiouyåäöAEIOUYÅÄÖ"

ordet = input("Skriv ett ord: ")

rovarsprak = ""

for bokstav in ordet:
    if bokstav.lower() not in vokaler and bokstav.isalpha():
        rovarsprak += bokstav + "o" + bokstav
    else:
        rovarsprak += bokstav

print(rovarsprak)
