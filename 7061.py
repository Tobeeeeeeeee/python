gissningar = 0
while True:
    gissning = input("Gissa på ett tal: ")
    if int(gissning) == 4:
        gissningar += 1
        break
    else:
        gissningar += 1
        print("Du gissade fel. Gissa på ett annat tal.")
print(f"Du gissade rätt!\nGissningar: {gissningar}")