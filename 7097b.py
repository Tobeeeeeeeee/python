lista = ['ananas', 'avokado', 'bakpulver', 'potatis', 'ostkaka']

antal_a = 0

for ord in lista:
    
    for bokstav in ord:
        
        if bokstav == 'a':
            antal_a = antal_a + 1

print("Antal 'a':", antal_a)
