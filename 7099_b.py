import random

tärningskast = [random.randint(1, 6) for _ in range(5)]

antal_ettor = tärningskast.count(1)

print("Tärningskast:", tärningskast)
print(f"Antal ettor: {antal_ettor}")
