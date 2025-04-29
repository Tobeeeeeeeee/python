import random
from collections import Counter

tärningskast = [random.randint(1, 6) for _ in range(10)]

sorterade_kast = sorted(tärningskast)

summa = sum(tärningskast)
medelvärde = summa / len(tärningskast)
minsta = min(tärningskast)
största = max(tärningskast)
antal_sexor = tärningskast.count(6)
vanligast = Counter(tärningskast).most_common(1)[0][0]

print("Tärningsresultat:", tärningskast)
print("Sorterade kast:", sorterade_kast)
print(f"Summa: {summa}")
print(f"Medelvärde: {medelvärde:.1f}")
print(f"Minsta värde: {minsta}")
print(f"Största värde: {största}")
print(f"Antal sexor: {antal_sexor}")
print(f"Vanligaste valör: {vanligast}")
