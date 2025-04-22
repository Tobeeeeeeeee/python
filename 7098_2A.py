def caesar_chiffer(text):
    resultat = ""
    for tecken in text:
        if 'a' <= tecken <= 'z':
            # Flytta bokstaven ett steg framåt, a blir b, z blir a
            ny = chr((ord(tecken) - ord('a') + 1) % 26 + ord('a'))
            resultat += ny
        elif 'A' <= tecken <= 'Z':
            ny = chr((ord(tecken) - ord('A') + 1) % 26 + ord('A'))
            resultat += ny
        else:
            # Behåll special tecken som dem är.
            resultat += tecken
    return resultat

text = input("Skriv texten du vill chiffrera: ")
krypterad = caesar_chiffer(text)
print("Krypterad text:", krypterad)
