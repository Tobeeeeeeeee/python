# Tobias J Loggbok

---

## 2025-04-29

Övat på att kasta tärningar i Python, räkna antalet ettor och skriva ut resultatet. Jag använde en list comprehension för att skapa en lista med fem slumptal mellan 1 och 6. Sedan använde jag `count(1)` för att räkna hur många ettor som fanns i listan och `print()` för att visa både tärningskasten och antalet ettor.

Kodexempel:
```python
import random

tärningskast = [random.randint(1, 6) for _ in range(5)]
antal_ettor = tärningskast.count(1)
print("Tärningskast:", tärningskast)
print(f"Antal ettor: {antal_ettor}")
```

---

## 2025-04-22

Idag har jag övat på att skriva ett program som översätter ord till rövarspråket. Jag fick mata in ett ord och programmet gick igenom varje bokstav: om det var en konsonant lade den till bokstaven + "o" + bokstaven igen, annars behölls bokstaven som den var. Jag använde for-loop för att gå igenom strängen, if-sats för att skilja på vokaler och konsonanter, och byggde upp en ny sträng med resultatet. Jag använde också `input()` för att ta emot användarens ord och `print()` för att visa översättningen.

---

## 2025-03-18

Övat på listor, index, `len`, `append`, `extend`, `insert`, `remove`, `pop` och `sort`.

---

## 2024-08-27

Jag har installerat VS Codium.

```python
print(2 + 2) # addition
print(2 - 2) # subtraktion
print(2 * 2) # multiplikation
print(2 / 2) # division
print(2 ** 2)# exponent
print(2 % 2)# modulus
print(2 //2)# heltals division

type(10) = class int
type("råtta") = string
type(True) = bool
type(3.8) = float
```

---